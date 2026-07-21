# Data Structures - Queue
# -----------------------------------------------------------------------------
# A queue is a First-In, First-Out (FIFO) collection.
# Think of a line at a store: first person in is first person served.
#
# Key concepts:
# 1. enqueue — add to back
# 2. dequeue — remove from front
# 3. deque — double-ended queue, O(1) on both ends
# 4. Practical uses — task scheduling, BFS traversal, message buffers
#
# Use collections.deque for queues — list.pop(0) is O(n).
# While deque.popleft() is o(1)
# -----------------------------------------------------------------------------


from collections import deque

# =============================================================================
# Queue
# =============================================================================


class Queue:
    def __init__(self):
        self._items: deque = deque()

    def enqueue(self, item) -> None:
        self._items.append(item)

    def dequeue(self):
        if self.is_empty:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"


# =============================================================================
# Practical: Task Scheduler
# =============================================================================


class TaskScheduler:
    def __init__(self):
        self._pending = Queue()

    def submit(self, task: str) -> None:
        self._pending.enqueue(task)

    def run_next(self) -> str | None:
        if self._pending.is_empty:
            return None
        return self._pending.dequeue()


# =============================================================================
# Practical: BFS Level Order (preview — full graph BFS in DS_06)
# =============================================================================


def bfs_tree_levels(tree: dict, root: str) -> list[list[str]]:
    """Breadth-first traversal returning nodes level by level."""
    if root not in tree:
        return []

    levels: list[list[str]] = []
    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty:
        level_size = len(queue)
        level: list[str] = []
        for _ in range(level_size):
            node = queue.dequeue()
            level.append(node)
            for child in tree.get(node, []):
                queue.enqueue(child)
        levels.append(level)

    return levels


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Queue Operations ===")
    queue = Queue()
    for item in ["A", "B", "C"]:
        queue.enqueue(item)
        print(f"  enqueued {item}: {queue}")
    print(f"  dequeued: {queue.dequeue()}")
    print(f"  after dequeue: {queue}")

    print("\n=== Task Scheduler ===")
    scheduler = TaskScheduler()
    for task in ["send email", "backup db", "generate report"]:
        scheduler.submit(task)
    while True:
        task = scheduler.run_next()
        if task is None:
            break
        print(f"  running: {task}")

    print("\n=== BFS Level Order ===")
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": [],
    }
    for level_num, nodes in enumerate(bfs_tree_levels(tree, "A"), start=1):
        print(f"  level {level_num}: {nodes}")


if __name__ == "__main__":
    main()
