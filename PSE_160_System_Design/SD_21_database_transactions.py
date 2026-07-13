# System Design - Distributed Transactions (Two-Phase Commit)
# -----------------------------------------------------------------------------
# In a single database, ACID transactions guarantee consistency. But in
# distributed systems, data is spread across multiple databases. How do
# you maintain consistency across them?
#
# Two-Phase Commit (2PC) is a protocol that ensures all participants
# in a distributed transaction either ALL commit or ALL abort.
#
# -----------------------------------------------------------------------------
# The Problem:
#
#   Transfer $100 from Account A (Database 1) to Account B (Database 2)
#
#   If Database 1 commits debit but Database 2 fails to credit → money lost
#   If Database 1 aborts debit but Database 2 credits → money created
#
#   We need BOTH to succeed or BOTH to fail.
#
# -----------------------------------------------------------------------------
# Two-Phase Commit Protocol:
#
#   Phase 1: PREPARE (Voting)
#     Coordinator asks all participants: "Can you commit?"
#     Each participant:
#       - Acquires locks
#       - Writes to local log (WAL)
#       - Responds YES (ready) or NO (abort)
#
#   Phase 2: COMMIT / ABORT (Decision)
#     If ALL participants said YES → Coordinator sends COMMIT
#     If ANY participant said NO  → Coordinator sends ABORT
#     Participants apply the decision
#
# -----------------------------------------------------------------------------
# Timeline:
#
#   Coordinator          Participant 1       Participant 2
#       │                    │                   │
#       │── PREPARE ────────▶│                   │
#       │── PREPARE ───────────────────────────▶│
#       │◀──── YES ──────────│                   │
#       │◀──── YES ─────────────────────────────│
#       │                    │                   │
#       │── COMMIT ─────────▶│                   │
#       │── COMMIT ───────────────────────────▶│
#       │◀──── ACK ──────────│                   │
#       │◀──── ACK ─────────────────────────────│
#       │                    │                   │
#
# -----------------------------------------------------------------------------
# Failure Modes:
#
# 1. Participant crashes before voting → Coordinator times out, aborts
# 2. Participant crashes after YES vote → Coordinator waits, blocks
# 3. Coordinator crashes after COMMIT decision → Participants hold locks
# 4. Network partition → Timeout, coordinator may retry or abort
#
# -----------------------------------------------------------------------------
# Alternatives to 2PC:
#
# - 3PC (Three-Phase Commit): Adds pre-commit phase, reduces blocking
# - Saga Pattern: Compensating transactions instead of locks
# - TCC (Try-Confirm-Cancel): Application-level two-phase
# - Event Sourcing + CQRS: Eventual consistency via event log
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - XA transactions (MySQL, PostgreSQL, Oracle)
# - Google Spanner (TrueTime + 2PC-like)
# - Amazon DynamoDB Transactions (2PC under the hood)
# - Banking systems, distributed databases
# -----------------------------------------------------------------------------


from enum import Enum
from typing import Any, Dict, List

# =============================================================================
# Transaction State
# =============================================================================


class TxState(Enum):
    INIT = "init"
    PREPARING = "preparing"
    PREPARED = "prepared"
    COMMITTING = "committing"
    COMMITTED = "committed"
    ABORTING = "aborting"
    ABORTED = "aborted"


# =============================================================================
# Participant (Database)
# =============================================================================


class Participant:
    """
    A database node participating in a distributed transaction.
    Manages local state and WAL (Write-Ahead Log).
    """

    def __init__(self, name: str, balance: float = 0.0):
        self.name = name
        self.balance = balance
        self.wal: List[str] = []
        self.state = TxState.INIT
        self.locked = False
        self.should_fail_prepare = False  # Simulate prepare failure

    def prepare(self, tx_id: str) -> bool:
        """Phase 1: Can this participant commit?"""
        self.state = TxState.PREPARING

        if self.should_fail_prepare:
            self.state = TxState.ABORTED
            self.wal.append(f"[{tx_id}] PREPARE → NO (simulated failure)")
            print(f"    [{self.name}] PREPARE → NO (simulated failure)")
            return False

        # Acquire lock and write to WAL
        self.locked = True
        self.state = TxState.PREPARED
        self.wal.append(f"[{tx_id}] PREPARE → YES")
        print(f"    [{self.name}] PREPARE → YES (locked, WAL written)")
        return True

    def commit(self, tx_id: str):
        """Phase 2: Apply the transaction."""
        self.state = TxState.COMMITTING
        self.wal.append(f"[{tx_id}] COMMIT")
        self.state = TxState.COMMITTED
        self.locked = False
        print(f"    [{self.name}] COMMITTED — balance={self.balance}")

    def abort(self, tx_id: str):
        """Phase 2: Roll back the transaction."""
        self.state = TxState.ABORTING
        self.wal.append(f"[{tx_id}] ABORT")
        self.state = TxState.ABORTED
        self.locked = False
        print(f"    [{self.name}] ABORTED — rolled back")

    def apply_operation(self, operation: Dict[str, Any]):
        """Apply a pending operation (used before prepare for demo)."""
        op_type = operation.get("type")
        amount = operation.get("amount", 0)
        if op_type == "debit":
            self.balance -= amount
        elif op_type == "credit":
            self.balance += amount

    def get_state(self) -> Dict[str, Any]:
        return {
            "balance": self.balance,
            "state": self.state.value,
            "locked": self.locked,
            "wal_entries": len(self.wal),
        }


# =============================================================================
# Transaction Coordinator
# =============================================================================


class TransactionCoordinator:
    """
    Coordinates the Two-Phase Commit protocol across participants.
    Manages the prepare/commit/abort lifecycle.
    """

    def __init__(self):
        self.transactions: Dict[str, Dict[str, Any]] = {}

    def execute_2pc(
        self,
        tx_id: str,
        participants: List[Participant],
        operations: Dict[str, Dict[str, Any]],
    ) -> bool:
        """
        Execute a Two-Phase Commit transaction.

        Args:
            tx_id: Unique transaction ID
            participants: List of database participants
            operations: {participant_name: operation_dict}
        """
        print(f"\n  [Coordinator] Starting 2PC for transaction '{tx_id}'")
        print(f"  [Coordinator] Participants: {[p.name for p in participants]}")

        # =====================================================================
        # Phase 1: PREPARE
        # =====================================================================
        print("\n  ── Phase 1: PREPARE ──")
        votes = {}
        all_yes = True

        for participant in participants:
            result = participant.prepare(tx_id)
            votes[participant.name] = result
            if not result:
                all_yes = False

        # =====================================================================
        # Phase 2: COMMIT or ABORT
        # =====================================================================
        print("\n  ── Phase 2: DECISION ──")

        if all_yes:
            print("  [Coordinator] ALL participants voted YES → COMMIT")

            # Apply operations
            for participant in participants:
                if participant.name in operations:
                    participant.apply_operation(operations[participant.name])

            # Commit all
            for participant in participants:
                participant.commit(tx_id)

            print(f"\n  [Coordinator] Transaction '{tx_id}' COMMITTED")
            return True
        else:
            print("  [Coordinator] At least one NO vote → ABORT")

            for participant in participants:
                participant.abort(tx_id)

            print(f"\n  [Coordinator] Transaction '{tx_id}' ABORTED")
            return False


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=" * 65)
    print("DISTRIBUTED TRANSACTIONS — Two-Phase Commit (2PC)")
    print("=" * 65)

    # --- 1. Successful transaction ---
    print("\n" + "-" * 65)
    print("1. SUCCESSFUL TRANSACTION")
    print("   Transfer $100 from Account A → Account B")
    print("-" * 65)

    coordinator = TransactionCoordinator()
    account_a = Participant("Account-A", balance=500.0)
    account_b = Participant("Account-B", balance=200.0)

    print(f"\n  Before: A={account_a.balance}, B={account_b.balance}")

    coordinator.execute_2pc(
        tx_id="TX-001",
        participants=[account_a, account_b],
        operations={
            "Account-A": {"type": "debit", "amount": 100},
            "Account-B": {"type": "credit", "amount": 100},
        },
    )

    print(f"\n  After:  A={account_a.balance}, B={account_b.balance}")
    print(f"  Sum:    {account_a.balance + account_b.balance} (must equal 700)")

    # --- 2. Failed participant ---
    print("\n" + "-" * 65)
    print("2. FAILED PARTICIPANT — Transaction aborted")
    print("   Account-B simulates prepare failure")
    print("-" * 65)

    account_a2 = Participant("Account-A", balance=500.0)
    account_b2 = Participant("Account-B", balance=200.0)
    account_b2.should_fail_prepare = True  # Simulate failure

    print(f"\n  Before: A={account_a2.balance}, B={account_b2.balance}")

    coordinator.execute_2pc(
        tx_id="TX-002",
        participants=[account_a2, account_b2],
        operations={
            "Account-A": {"type": "debit", "amount": 100},
            "Account-B": {"type": "credit", "amount": 100},
        },
    )

    print(f"\n  After:  A={account_a2.balance}, B={account_b2.balance}")
    print("  (Balances unchanged — transaction rolled back)")

    # --- 3. WAL inspection ---
    print("\n" + "-" * 65)
    print("3. WRITE-AHEAD LOG (WAL)")
    print("   Each participant logs every step for crash recovery")
    print("-" * 65)

    print("\n  Account-A WAL:")
    for entry in account_a.wal:
        print(f"    {entry}")
    print("\n  Account-B WAL:")
    for entry in account_b.wal:
        print(f"    {entry}")

    # --- 4. Three participants ---
    print("\n" + "-" * 65)
    print("4. MULTI-PARTICIPANT — 3 databases")
    print("-" * 65)

    db1 = Participant("DB-Orders", balance=0)
    db2 = Participant("DB-Inventory", balance=10)
    db3 = Participant("DB-Payments", balance=1000)

    print(
        f"\n  Before: Orders={db1.balance}, Inventory={db2.balance}, Payments={db3.balance}"
    )

    coordinator.execute_2pc(
        tx_id="TX-003",
        participants=[db1, db2, db3],
        operations={
            "DB-Orders": {"type": "credit", "amount": 1},
            "DB-Inventory": {"type": "debit", "amount": 1},
            "DB-Payments": {"type": "debit", "amount": 50},
        },
    )

    print(
        f"\n  After:  Orders={db1.balance}, Inventory={db2.balance}, Payments={db3.balance}"
    )

    # --- Summary ---
    print("\n" + "=" * 65)
    print("SUMMARY — Two-Phase Commit")
    print("=" * 65)
    print("""
  Phase    What happens              Failure handling
  -----    ------------              ----------------
  PREPARE  Participants vote YES/NO  Timeout → treat as NO
  COMMIT   Apply if all YES          Coordinator retry / WAL recovery
           Abort if any NO           Rollback all participants

  Pros:
  + Strong consistency (all-or-nothing)
  + Well-understood protocol
  + Used by XA transactions in most databases

  Cons:
  - Blocking: Participants hold locks until commit/abort
  - Coordinator SPOF: If coordinator crashes mid-protocol
  - Performance: Two round-trips, synchronous
  - Not suitable for high-throughput systems

  Alternatives:
  - Saga: Compensating transactions (eventual consistency)
  - TCC: Try-Confirm-Cancel (application-level)
  - Event Sourcing: Append-only log, replay to rebuild state
""")


if __name__ == "__main__":
    main()
