# Data Structures - Trees
# -----------------------------------------------------------------------------
# A tree is a hierarchical data structure with a root node and child nodes.
# Binary trees have at most two children per node.
#
# Key concepts:
# 1. Node — stores a value and references to children.
# 2. Binary Search Tree (BST) — left < root < right.
# 3. Traversals — in-order, pre-order, post-order.
# 4. Practical uses — file systems, databases, expression parsing.
# -----------------------------------------------------------------------------


# =============================================================================
# Binary Tree Node
# =============================================================================


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


# =============================================================================
# Binary Search Tree
# =============================================================================


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    # Traversals
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)

    def pre_order(self):
        result = []
        self._pre_order(self.root, result)
        return result

    def _pre_order(self, node, result):
        if node:
            result.append(node.value)
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)

    def post_order(self):
        result = []
        self._post_order(self.root, result)
        return result

    def _post_order(self, node, result):
        if node:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(node.value)


# =============================================================================
# Usage
# =============================================================================


def main():
    bst = BinarySearchTree()
    for value in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(value)

    print("=== BST Traversals ===")
    print(f"  In-order (sorted): {bst.in_order()}")
    print(f"  Pre-order:         {bst.pre_order()}")
    print(f"  Post-order:        {bst.post_order()}")

    print("\n=== Search ===")
    print(f"  Search 4: {bst.search(4)}")
    print(f"  Search 9: {bst.search(9)}")


if __name__ == "__main__":
    main()
