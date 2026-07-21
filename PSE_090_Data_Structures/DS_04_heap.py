# Data Structures - Heap
# -----------------------------------------------------------------------------
# A heap is a complete binary tree where parents are ordered relative to
# children. Python's heapq module provides a min-heap implementation.
#
# Key concepts:
# 1. Min-heap — parent <= children
# 2. heapq module — heap operations on lists
# 3. Heapify — convert list to heap in O(n)
# 4. Use cases — priority queues, top-K problems
# -----------------------------------------------------------------------------


# =============================================================================
# heapq Basics
# =============================================================================


import heapq

# Create heap from list
heap = [5, 3, 8, 1, 2]
heapq.heapify(heap)
print(f"Heapified: {heap}")

# Push and pop
heapq.heappush(heap, 0)
print(f"After push 0: {heap}")

smallest = heapq.heappop(heap)
print(f"Pop smallest: {smallest}, remaining: {heap}")


# =============================================================================
# Build Heap from Scratch
# =============================================================================


heap = []
for value in [10, 4, 15, 1, 7]:
    heapq.heappush(heap, value)

print(f"Heap: {heap}")
print(f"Smallest: {heap[0]}")


# =============================================================================
# Top-K Elements
# =============================================================================


def top_k(numbers, k):
    """Find K largest elements."""
    return heapq.nlargest(k, numbers)


def bottom_k(numbers, k):
    """Find K smallest elements."""
    return heapq.nsmallest(k, numbers)


data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Top 3: {top_k(data, 3)}")
print(f"Bottom 3: {bottom_k(data, 3)}")


# =============================================================================
# Priority Queue
# =============================================================================


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0

    def push(self, priority, item):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._heap)[-1]

    def __len__(self):
        return len(self._heap)


pq = PriorityQueue()
pq.push(3, "low")
pq.push(1, "high")
pq.push(2, "medium")

while len(pq):
    print(f"  Process: {pq.pop()}")


def main():
    print("=== Heap ===")
    data = [20, 5, 15, 10, 1]
    heapq.heapify(data)
    print(f"Heap: {data}")
    print(f"Top 2: {heapq.nlargest(2, data)}")


if __name__ == "__main__":
    main()
