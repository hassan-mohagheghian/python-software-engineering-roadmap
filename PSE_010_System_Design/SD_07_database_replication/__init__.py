# System Design - Database Replication
# -----------------------------------------------------------------------------
# Database Replication is the process of copying data from one database
# (Primary) to one or more Replica databases.
#
# Replication improves:
#
# - High availability
# - Read scalability
# - Fault tolerance
# - Disaster recovery
#
# -----------------------------------------------------------------------------
# Architecture
#
#                    WRITE
#          +----------------------+
#          |                      |
#          v                      |
#      +-----------+              |
#      | Primary DB|              |
#      +-----------+              |
#         |      |                |
#         |      | Replication    |
#         |      +----------------------------+
#         |                                   |
#         v                                   v
#   +-------------+                    +-------------+
#   | Replica DB1 |                    | Replica DB2 |
#   +-------------+                    +-------------+
#         ^                                   ^
#         |                                   |
#         +------------ READS -----------------+
#
# -----------------------------------------------------------------------------
# In this example:
#
# - The Primary database accepts all writes.
# - Every write is replicated to all replicas.
# - Read requests are distributed across replicas
#   using a simple round-robin strategy.
#
# This is a simplified simulation of database replication.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------


class Database:
    def __init__(self, name: str):
        self.name = name
        self.storage = {}

    def write(self, key: str, value: str):
        self.storage[key] = value
        print(f"[{self.name}] WRITE  {key} -> {value}")

    def read(self, key: str):
        value = self.storage.get(key)

        print(f"[{self.name}] READ   {key} -> {value}")

        return value


# -----------------------------------------------------------------------------
# Replication Manager
# -----------------------------------------------------------------------------


class ReplicationManager:
    """
    Simulates database replication.

    - Writes always go to the Primary.
    - Reads come from Replicas.
    """

    def __init__(self):
        self.primary = Database("Primary")

        self.replicas = [
            Database("Replica-1"),
            Database("Replica-2"),
        ]

        self.index = 0

    # -------------------------------------------------------------------------
    # Write
    # -------------------------------------------------------------------------

    def write(self, key: str, value: str):
        print("\nClient writes data")

        # Step 1
        self.primary.write(key, value)

        # Step 2
        print("Replicating...")

        for replica in self.replicas:
            replica.write(key, value)

    # -------------------------------------------------------------------------
    # Read
    # -------------------------------------------------------------------------

    def read(self, key: str):
        replica = self.replicas[self.index]

        self.index = (self.index + 1) % len(self.replicas)

        print("\nClient reads data")

        return replica.read(key)


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    replication = ReplicationManager()

    replication.write("user:1", "Alice")
    replication.write("user:2", "Bob")

    replication.read("user:1")
    replication.read("user:2")
    replication.read("user:1")
    replication.read("user:2")


if __name__ == "__main__":
    main()
