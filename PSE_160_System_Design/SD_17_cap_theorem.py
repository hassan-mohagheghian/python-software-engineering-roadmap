# System Design - CAP Theorem
# -----------------------------------------------------------------------------
# The CAP Theorem (Brewer's Theorem) states that a distributed data store
# can only provide TWO of the following three guarantees simultaneously:
#
#   C - Consistency
#   A - Availability
#   P - Partition Tolerance
#
# Every distributed system MUST handle network partitions (P), so the real
# choice is between Consistency and Availability during a partition.
#
# -----------------------------------------------------------------------------
# The Three Guarantees:
#
#   Consistency (C):
#     Every read receives the most recent write or an error.
#     All nodes see the same data at the same time.
#
#   Availability (A):
#     Every request receives a non-error response (no timeout).
#     The system is always operational, even if nodes are down.
#
#   Partition Tolerance (P):
#     The system continues to operate despite network partitions
#     (communication breaks between nodes).
#
# -----------------------------------------------------------------------------
# The Trade-off:
#
#   In a distributed system, network partitions WILL happen (P is mandatory).
#   So the real choice during a partition is:
#
#     CP: Consistent but may reject requests
#         → Choose correctness over uptime
#         → Example: Banking systems, Zookeeper, etcd
#
#     AP: Available but may serve stale data
#         → Choose uptime over immediate correctness
#         → Example: DNS, Cassandra, DynamoDB, social media feeds
#
#   CA (without partitions): Only possible in single-node systems
#     → Both consistency and availability, but no network resilience
#     → Not practical for distributed systems
#
# -----------------------------------------------------------------------------
# CAP Triangle:
#
#           Partition Tolerance (P)
#                      ▲
#                     / \
#                    /   \
#                   /     \
#                  /       \
#                 /         \
#        [ CP ]  /           \  [ AP ]
# Consistency + /             \ Availability +
# Partition    /               \ Partition
#             / <-------------> \
#            /  [The Trade-Off]  \
#           /                     \
#          /                       \
#         /                         \
#        ▲                           ▲
#       / \                         / \
#      /   \                       /   \
#     /  C  \                     /  A  \
#    ───────                     ───────
#  Consistency                 Availability

#            \─────────────────/
#                    [ CA ]
#           Consistency + Availability
#
# -----------------------------------------------------------------------------
# Real-world Examples:
#
#   CP Systems (Consistency + Partition Tolerance):
#     - HBase, MongoDB (with majority write concern)
#     - Zookeeper, etcd, Consul
#     - Traditional RDBMS with replication (PostgreSQL sync)
#     - Trade-off: Reject requests when partitioned
#
#   AP Systems (Availability + Partition Tolerance):
#     - Cassandra, DynamoDB, CouchDB
#     - DNS, NTP
#     - Social media feeds, shopping carts
#     - Trade-off: Serve potentially stale data
#
#   CA Systems (Consistency + Availability):
#     - Single-node PostgreSQL, single-node MySQL
#     - Not distributed — cannot survive node failure
# -----------------------------------------------------------------------------
# Beyond CAP — PACELC:
#
#   PACELC extends CAP: even when there's NO partition, you still face
#   a trade-off between Latency and Consistency.
#
#     If Partition → choose A or C (CAP)
#     Else   → choose L (low latency) or C (strong consistency)
#
#   Example:
#     - Cassandra: EL (prefer latency, eventually consistent)
#     - Spanner:   EC (prefer consistency, higher latency)
# -----------------------------------------------------------------------------


import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional

# =============================================================================
# Consistency Levels
# =============================================================================


class ConsistencyLevel(Enum):
    """
    Levels of consistency a system can offer.
    Higher levels = more consistency but higher latency / lower availability.
    """

    STRONG = "strong"  # All nodes see same data immediately
    EVENTUAL = "eventual"  # Nodes will converge eventually
    WEAK = "weak"  # No guarantees across nodes


# =============================================================================
# Node
# =============================================================================


@dataclass
class Node:
    """
    A single node in a distributed system.
    Each node maintains its own copy of the data.
    """

    node_id: str
    data: Dict[str, Any] = field(default_factory=dict)
    is_alive: bool = True
    latency_ms: float = 0.0

    def read(self, key: str) -> Optional[Any]:
        if not self.is_alive:
            raise ConnectionError(f"Node {self.node_id} is down")
        return self.data.get(key)

    def write(self, key: str, value: Any):
        if not self.is_alive:
            raise ConnectionError(f"Node {self.node_id} is down")
        self.data[key] = value


# =============================================================================
# CP System (Consistency + Partition Tolerance)
# =============================================================================


class CPSystem:
    """
    A system that prioritizes CONSISTENCY over AVAILABILITY during partitions.
    During a network partition, some requests will be rejected to maintain
    data correctness.
    """

    def __init__(self, consistency: ConsistencyLevel = ConsistencyLevel.STRONG):
        self.nodes: Dict[str, Node] = {}
        self.consistency = consistency
        self.partition_active = False

    def add_node(self, node_id: str, latency_ms: float = 10.0):
        self.nodes[node_id] = Node(node_id, latency_ms=latency_ms)

    def simulate_partition(self):
        """Simulate a network partition (node isolation)."""
        self.partition_active = True
        # Simulate: mark random node as unreachable
        nodes = list(self.nodes.values())
        if len(nodes) > 1:
            isolated = random.choice(nodes[1:])
            isolated.is_alive = False
            print(f"  [Partition] Node '{isolated.node_id}' is now isolated")

    def heal_partition(self):
        """Heal the network partition."""
        self.partition_active = False
        for node in self.nodes.values():
            node.is_alive = True
        print("  [Partition] Network partition healed")

    def write(self, key: str, value: Any) -> bool:
        """
        Write to majority of nodes. Fails if majority is unreachable.
        This ensures consistency — if we can't confirm majority, we reject.
        """
        alive_nodes = [n for n in self.nodes.values() if n.is_alive]
        majority_needed = (len(self.nodes) // 2) + 1

        if len(alive_nodes) < majority_needed:
            print(
                f"  [CP Write] REJECTED — only {len(alive_nodes)}/{len(self.nodes)} "
                f"nodes available (need {majority_needed} for majority)"
            )
            return False

        # Write to all alive nodes (in real systems, this would be quorum write)
        for node in alive_nodes:
            node.write(key, value)
        print(
            f"  [CP Write] '{key}' = '{value}' written to "
            f"{len(alive_nodes)}/{len(self.nodes)} nodes"
        )
        return True

    def read(self, key: str) -> Optional[Any]:
        """
        Read from majority of nodes and return the latest value.
        Fails if majority is unreachable.
        """
        alive_nodes = [n for n in self.nodes.values() if n.is_alive]
        majority_needed = (len(self.nodes) // 2) + 1

        if len(alive_nodes) < majority_needed:
            print(
                f"  [CP Read] REJECTED — only {len(alive_nodes)}/{len(self.nodes)} "
                f"nodes available"
            )
            return None

        # Read from all alive nodes (in real systems, read from quorum)
        values = {}
        for node in alive_nodes:
            val = node.read(key)
            if val is not None:
                values[key] = val

        return values.get(key)


# =============================================================================
# AP System (Availability + Partition Tolerance)
# =============================================================================


class APSystem:
    """
    A system that prioritizes AVAILABILITY over CONSISTENCY during partitions.
    During a network partition, all requests are served — but may return stale data.
    Uses "last-write-wins" or vector clocks for conflict resolution.
    """

    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.partition_active = False
        self.vector_clocks: Dict[str, int] = {}  # key -> logical timestamp

    def add_node(self, node_id: str, latency_ms: float = 10.0):
        self.nodes[node_id] = Node(node_id, latency_ms=latency_ms)

    def simulate_partition(self):
        """Simulate a network partition."""
        self.partition_active = True
        nodes = list(self.nodes.values())
        if len(nodes) > 1:
            isolated = random.choice(nodes[1:])
            isolated.is_alive = False
            print(f"  [Partition] Node '{isolated.node_id}' is now isolated")

    def heal_partition(self):
        """Heal the network partition and sync nodes."""
        self.partition_active = False
        for node in self.nodes.values():
            node.is_alive = True
        print("  [Partition] Network partition healed")
        self._sync_nodes()

    def _sync_nodes(self):
        """
        After partition heals, sync all nodes to the latest value.
        Uses "last-write-wins" based on vector clock.
        """
        latest_value = None
        latest_clock = -1

        for node in self.nodes.values():
            for key, val in node.data.items():
                clock = self.vector_clocks.get(key, 0)
                if clock > latest_clock:
                    latest_clock = clock
                    latest_value = val

        if latest_value is not None:
            for node in self.nodes.values():
                for key in list(node.data.keys()):
                    node.data[key] = latest_value
            print("  [Sync] All nodes converged to latest value")

    def write(self, key: str, value: Any) -> bool:
        """
        Write to ALL available nodes. Always succeeds if at least one node
        is alive. This ensures availability.
        """
        alive_nodes = [n for n in self.nodes.values() if n.is_alive]

        if not alive_nodes:
            print("  [AP Write] FAILED — no nodes available")
            return False

        # Increment vector clock
        self.vector_clocks[key] = self.vector_clocks.get(key, 0) + 1

        # Write to all alive nodes (best-effort)
        for node in alive_nodes:
            node.write(key, value)

        unreachable = len(self.nodes) - len(alive_nodes)
        print(
            f"  [AP Write] '{key}' = '{value}' written to "
            f"{len(alive_nodes)}/{len(self.nodes)} nodes"
            f"{f' ({unreachable} unreachable)' if unreachable else ''}"
        )
        return True

    def read(self, key: str) -> Optional[Any]:
        """
        Read from ANY available node. Always succeeds if at least one node
        is alive — but may return stale data.
        """
        alive_nodes = [n for n in self.nodes.values() if n.is_alive]

        if not alive_nodes:
            print("  [AP Read] FAILED — no nodes available")
            return None

        # Read from first alive node (in real systems, read from local replica)
        node = alive_nodes[0]
        value = node.read(key)

        stale_warning = ""
        if len(alive_nodes) < len(self.nodes):
            stale_warning = " (may be stale — partition active)"

        print(
            f"  [AP Read] '{key}' = '{value}' from node '{node.node_id}'{stale_warning}"
        )
        return value


# =============================================================================
# CA System (Consistency + Availability, no Partition Tolerance)
# =============================================================================


class CASystem:
    """
    A system that provides both Consistency and Availability, but CANNOT
    handle network partitions. Only works on a single node (not truly distributed).
    """

    def __init__(self):
        self.node = Node(node_id="single-node")
        self.is_distributed = False  # Key limitation

    def write(self, key: str, value: Any):
        self.node.write(key, value)
        print(f"  [CA Write] '{key}' = '{value}' written")

    def read(self, key: str) -> Optional[Any]:
        value = self.node.read(key)
        print(f"  [CA Read] '{key}' = '{value}'")
        return value

    def simulate_partition(self):
        """
        CA systems CANNOT handle partitions.
        The entire system goes down if the node fails.
        """
        self.node.is_alive = False
        print("  [CA] Node failed — system is DOWN (no partition tolerance)")

    def heal_partition(self):
        self.node.is_alive = True
        print("  [CA] Node recovered")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=" * 65)
    print("CAP THEOREM — Distributed Systems Trade-offs")
    print("=" * 65)

    # -------------------------------------------------------------------------
    # 1. CP System (Consistency + Partition Tolerance)
    # -------------------------------------------------------------------------
    print("\n" + "-" * 65)
    print("1. CP SYSTEM — Consistency + Partition Tolerance")
    print("   (Rejects requests during partition to maintain correctness)")
    print("-" * 65)

    cp = CPSystem()
    cp.add_node("node-1")
    cp.add_node("node-2")
    cp.add_node("node-3")

    print("\n  Normal operation:")
    cp.write("account_balance", "$1000")
    cp.read("account_balance")

    print("\n  During partition (node isolated):")
    cp.simulate_partition()
    cp.write("account_balance", "$1500")  # May fail if majority unreachable
    cp.read("account_balance")

    print("\n  After partition heals:")
    cp.heal_partition()
    cp.write("account_balance", "$2000")
    cp.read("account_balance")

    # -------------------------------------------------------------------------
    # 2. AP System (Availability + Partition Tolerance)
    # -------------------------------------------------------------------------
    print("\n" + "-" * 65)
    print("2. AP SYSTEM — Availability + Partition Tolerance")
    print("   (Always serves requests, may return stale data)")
    print("-" * 65)

    ap = APSystem()
    ap.add_node("node-1")
    ap.add_node("node-2")
    ap.add_node("node-3")

    print("\n  Normal operation:")
    ap.write("cart_item", "laptop")
    ap.read("cart_item")

    print("\n  During partition (node isolated):")
    ap.simulate_partition()
    ap.write("cart_item", "phone")  # Always succeeds
    ap.read("cart_item")  # May be stale

    print("\n  After partition heals (nodes converge):")
    ap.heal_partition()
    ap.read("cart_item")

    # -------------------------------------------------------------------------
    # 3. CA System (Consistency + Availability, no Partition Tolerance)
    # -------------------------------------------------------------------------
    print("\n" + "-" * 65)
    print("3. CA SYSTEM — Consistency + Availability (single node)")
    print("   (Cannot handle partitions — not truly distributed)")
    print("-" * 65)

    ca = CASystem()

    print("\n  Normal operation:")
    ca.write("user_session", "abc123")
    ca.read("user_session")

    print("\n  Node failure (no partition tolerance):")
    ca.simulate_partition()
    try:
        ca.read("user_session")
    except ConnectionError as e:
        print(f"  [Error] {e}")

    print("\n  Node recovered:")
    ca.heal_partition()
    ca.read("user_session")

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------
    print("\n" + "=" * 65)
    print("SUMMARY — CAP Trade-offs")
    print("=" * 65)
    print("""
  System   Guarantees              Trade-off
  ------   ----------              ---------
  CP       Consistency +           Rejects requests when
           Partition Tolerance     partitioned (lower availability)

  AP       Availability +          May serve stale data during
           Partition Tolerance     partitions (lower consistency)

  CA       Consistency +           Cannot survive network
           Availability            partitions (single node only)

  In practice: P is mandatory in distributed systems.
  Choose CP for correctness (banking, inventory).
  Choose AP for uptime (social feeds, shopping carts).
""")


if __name__ == "__main__":
    main()
