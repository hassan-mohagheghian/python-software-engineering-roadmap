# Data Structures - Graphs
# -----------------------------------------------------------------------------
# A graph is a collection of nodes (vertices) connected by edges.
# Graphs can be directed or undirected, weighted or unweighted.
#
# Key concepts:
# 1. Adjacency list — dict of {node: [neighbors]}.
# 2. BFS — breadth-first search, explores level by level.
# 3. DFS — depth-first search, explores as deep as possible.
# 4. Practical uses — social networks, routing, dependencies.
# -----------------------------------------------------------------------------


from collections import deque

# =============================================================================
# Graph (Adjacency List)
# =============================================================================


class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        if not self.directed:
            self.adj.setdefault(v, []).append(u)

    def bfs(self, start):
        visited = []
        queue = deque([start])
        seen = {start}
        while queue:
            node = queue.popleft()
            visited.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return visited

    def dfs(self, start):
        visited = []
        stack = [start]
        seen = set()
        while stack:
            node = stack.pop()
            if node not in seen:
                seen.add(node)
                visited.append(node)
                for neighbor in self.adj.get(node, []):
                    if neighbor not in seen:
                        stack.append(neighbor)
        return visited

    def has_path(self, start, end):
        return end in self.bfs(start)

    def __repr__(self):
        return f"Graph({self.adj})"


# =============================================================================
# Usage
# =============================================================================


def main():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "F")
    g.add_edge("E", "F")

    print("=== Graph ===")
    print(f"  {g}")

    print("\n=== BFS from A ===")
    print(f"  {g.bfs('A')}")

    print("\n=== DFS from A ===")
    print(f"  {g.dfs('A')}")

    print("\n=== Path Check ===")
    print(f"  A → F: {g.has_path('A', 'F')}")
    print(f"  D → F: {g.has_path('D', 'F')}")


if __name__ == "__main__":
    main()
