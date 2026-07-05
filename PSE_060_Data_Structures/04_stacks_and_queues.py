# Data Structures - Stacks and Queues
# -----------------------------------------------------------------------------
# Stacks (LIFO) and Queues (FIFO) are fundamental abstract data types.
# Python's list works as a stack. collections.deque works as both.
#
# Key concepts:
# 1. Stack — push, pop, peek (last-in, first-out).
# 2. Queue — enqueue, dequeue (first-in, first-out).
# 3. Deque — double-ended queue, O(1) on both ends.
# 4. Practical uses — undo/redo, BFS, task scheduling.
# -----------------------------------------------------------------------------


from collections import deque


# =============================================================================
# Stack (using list)
# =============================================================================


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    @property
    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


def stack_demo():
    stack = Stack()
    for item in [1, 2, 3]:
        stack.push(item)
        print(f"  pushed {item}: {stack}")

    print(f"  peek: {stack.peek()}")
    print(f"  popped: {stack.pop()}")
    print(f"  after pop: {stack}")


# =============================================================================
# Queue (using deque)
# =============================================================================


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    @property
    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"


def queue_demo():
    queue = Queue()
    for item in ["A", "B", "C"]:
        queue.enqueue(item)
        print(f"  enqueued {item}: {queue}")

    print(f"  dequeued: {queue.dequeue()}")
    print(f"  after dequeue: {queue}")


# =============================================================================
# Practical: Balanced Parentheses (Stack)
# =============================================================================


def is_balanced(expression: str) -> bool:
    stack = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty or stack.pop() != pairs[char]:
                return False
    return stack.is_empty


# =============================================================================
# Practical: BFS Traversal (Queue)
# =============================================================================


def bfs(graph: dict, start: str) -> list:
    visited = []
    queue = Queue()
    queue.enqueue(start)
    while not queue.is_empty:
        node = queue.dequeue()
        if node not in visited:
            visited.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
    return visited


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Stack ===")
    stack_demo()

    print("\n=== Queue ===")
    queue_demo()

    print("\n=== Balanced Parentheses ===")
    print(f"  '(a + b) * [c]': {is_balanced('(a + b) * [c]')}")
    print(f"  '(a + b':        {is_balanced('(a + b')}")
    print(f"  '{{[()]}}':       {is_balanced('{[()]}')}")

    print("\n=== BFS Traversal ===")
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print(f"  BFS from A: {bfs(graph, 'A')}")


if __name__ == "__main__":
    main()
