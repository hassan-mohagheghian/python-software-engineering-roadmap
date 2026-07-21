# Data Structures - Linked List
# -----------------------------------------------------------------------------
# A linked list is a sequence of nodes where each node points to the next.
# Unlike arrays, elements are not stored in contiguous memory.
#
# Key concepts:
# 1. Node structure (value + next pointer)
# 2. Singly linked list
# 3. Insertion and deletion
# 4. Traversal
# -----------------------------------------------------------------------------


# =============================================================================
# Node
# =============================================================================


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


# =============================================================================
# Singly Linked List
# =============================================================================


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        """Add to end of list."""
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self._size += 1

    def prepend(self, value):
        """Add to beginning of list."""
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1

    def remove(self, value):
        """Remove first occurrence of value."""
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next

    def find(self, value):
        """Return node with value, or None."""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def __len__(self):
        return self._size

    def __repr__(self):
        items = []
        current = self.head
        while current:
            items.append(repr(current.value))
            current = current.next
        return " -> ".join(items) + " -> None"


# =============================================================================
# Usage
# =============================================================================


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)

print(f"List: {ll}")
print(f"Length: {len(ll)}")

ll.remove(2)
print(f"After remove(2): {ll}")

node = ll.find(3)
print(f"Find(3): {node.value if node else None}")


def main():
    print("=== Linked List ===")
    ll = LinkedList()
    for i in range(5):
        ll.append(i)
    print(f"List: {ll}")
    ll.remove(2)
    print(f"After remove: {ll}")


if __name__ == "__main__":
    main()
