# System Design - Consistent Hashing
# -----------------------------------------------------------------------------
# Consistent Hashing is a technique used to distribute requests or data across
# a dynamic set of server nodes.
#
# Unlike standard modulo hashing (hash(key) % N), where changing the number
# of servers (N) causes almost all keys to be redistributed, consistent hashing
# ensures that when servers are added or removed, only a small fraction of keys
# (K/N) are remapped.
#
# -----------------------------------------------------------------------------
# How it works:
#
# 1. Ring Space: Both keys and server nodes are mapped to a circular numerical
#    space (a hash ring).
# 2. Key Routing: To find which server holds a key, we hash the key and move
#    clockwise on the ring to find the first server node.
# 3. Virtual Nodes: To prevent unbalanced distribution (hotspots), each physical
#    node is hashed multiple times to create "virtual nodes" scattered across
#    the ring.
#
# -----------------------------------------------------------------------------
# High-Level Representation of the Hash Ring
#
#               [Node-A (vnode-0)]
#                  0 / 2^128
#                .          .
#             .                .
#     [Node-C]                  [Node-B]
#        .                          .
#         .                        .
#          .                      .
#           .                  .
#             [Node-A (vnode-1)]
# -----------------------------------------------------------------------------

import bisect
import hashlib

# -----------------------------------------------------------------------------
# Standard Modulo Hashing Ring (for comparison)
# -----------------------------------------------------------------------------


class ModuloHashRing:
    """
    Simulates standard modulo hashing: server = hash(key) % N.
    """

    def __init__(self):
        self.nodes: list[str] = []

    def add_node(self, node: str):
        if node not in self.nodes:
            self.nodes.append(node)
            self.nodes.sort()  # Keep sorted to ensure consistent index order

    def remove_node(self, node: str):
        if node in self.nodes:
            self.nodes.remove(node)

    def get_node(self, key: str) -> str | None:
        if not self.nodes:
            return None

        # MD5 is used for deterministic, system-independent hashing
        key_hash = int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)
        index = key_hash % len(self.nodes)
        return self.nodes[index]


# -----------------------------------------------------------------------------
# Consistent Hashing Ring
# -----------------------------------------------------------------------------


class ConsistentHashRing:
    """
    Simulates consistent hashing with support for virtual nodes.
    """

    def __init__(self, replicas: int = 5):
        self.replicas = replicas  # Number of virtual nodes per physical node
        self.ring: list[int] = []  # Sorted list of virtual node hashes
        self.hash_to_node: dict[
            int, str
        ] = {}  # Maps virtual node hash to physical node name

    def _hash(self, key: str) -> int:
        """Returns a 128-bit integer hash for a string key using MD5."""
        return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)

    def add_node(self, node: str):
        """
        Adds a physical node to the ring by generating and placing its virtual nodes.
        """
        for i in range(self.replicas):
            vnode_name = f"{node}#vnode-{i}"
            vnode_hash = self._hash(vnode_name)

            # Insert virtual node hash in sorted position
            idx = bisect.bisect_left(self.ring, vnode_hash)

            # Handle rare collision
            if idx < len(self.ring) and self.ring[idx] == vnode_hash:
                continue

            self.ring.insert(idx, vnode_hash)
            self.hash_to_node[vnode_hash] = node

        print(f"[Ring] Added node: {node} ({self.replicas} virtual nodes)")

    def remove_node(self, node: str):
        """
        Removes a physical node and all its virtual nodes from the ring.
        """
        for i in range(self.replicas):
            vnode_name = f"{node}#vnode-{i}"
            vnode_hash = self._hash(vnode_name)

            idx = bisect.bisect_left(self.ring, vnode_hash)
            if idx < len(self.ring) and self.ring[idx] == vnode_hash:
                self.ring.pop(idx)
                del self.hash_to_node[vnode_hash]

        print(f"[Ring] Removed node: {node}")

    def get_node(self, key: str) -> str | None:
        """
        Finds the first physical node encountered clockwise from the key's hash.
        """
        if not self.ring:
            return None

        key_hash = self._hash(key)

        # Locate the insert position clockwise
        idx = bisect.bisect_right(self.ring, key_hash)

        # If key_hash is greater than the largest hash in the ring, wrap around to 0
        if idx == len(self.ring):
            idx = 0

        return self.hash_to_node[self.ring[idx]]


# -----------------------------------------------------------------------------
# Usage & Simulation
# -----------------------------------------------------------------------------


def analyze_redistribution(
    title: str,
    ring_impl,
    keys: list[str],
    add_node_name: str | None = None,
    remove_node_name: str | None = None,
):
    """
    Simulates changing server topology and counts how many keys are remapped.
    """
    print(f"\n--- {title} ---")

    # 1. Initialize ring with Node-A, Node-B, Node-C
    ring = ring_impl
    for node in ["Node-A", "Node-B", "Node-C"]:
        ring.add_node(node)

    # 2. Get initial key-to-node mapping
    initial_mappings = {key: ring.get_node(key) for key in keys}

    # 3. Modify ring topology
    if add_node_name:
        ring.add_node(add_node_name)
    if remove_node_name:
        ring.remove_node(remove_node_name)

    # 4. Get new mapping and calculate remapped keys
    new_mappings = {key: ring.get_node(key) for key in keys}
    remapped_count = sum(
        1 for key in keys if initial_mappings[key] != new_mappings[key]
    )

    # 5. Display stats
    total_keys = len(keys)
    percentage = (remapped_count / total_keys) * 100
    print(f"Total Keys: {total_keys}")
    print(f"Remapped Keys: {remapped_count} ({percentage:.2f}%)")


def main():
    # 1,000 distinct data keys (e.g. user sessions or photo IDs)
    keys = [f"user_session_{i}" for i in range(1000)]

    print("=== SCENARIO 1: Adding a new node (Node-D) ===")

    # Compare Modulo Hashing vs Consistent Hashing when adding a node
    analyze_redistribution(
        title="Modulo Hashing (Adding Node-D)",
        ring_impl=ModuloHashRing(),
        keys=keys,
        add_node_name="Node-D",
    )

    analyze_redistribution(
        title="Consistent Hashing (Adding Node-D)",
        ring_impl=ConsistentHashRing(replicas=50),
        keys=keys,
        add_node_name="Node-D",
    )

    print("\n=============================================")
    print("=== SCENARIO 2: Removing an existing node (Node-C) ===")

    # Compare Modulo Hashing vs Consistent Hashing when removing a node
    analyze_redistribution(
        title="Modulo Hashing (Removing Node-C)",
        ring_impl=ModuloHashRing(),
        keys=keys,
        remove_node_name="Node-C",
    )

    analyze_redistribution(
        title="Consistent Hashing (Removing Node-C)",
        ring_impl=ConsistentHashRing(replicas=50),
        keys=keys,
        remove_node_name="Node-C",
    )


if __name__ == "__main__":
    main()
