# Data Structures - Stack
# -----------------------------------------------------------------------------
# A stack is a Last-In, First-Out (LIFO) collection.
# Think of a stack of plates: you add and remove from the top.
#
# Key concepts:
# 1. push — add to top
# 2. pop — remove from top
# 3. peek — view top without removing
# 4. Practical uses — undo/redo, call stack, balanced parentheses
#
# Python's list works well as a stack (append + pop).
# -----------------------------------------------------------------------------


# =============================================================================
# Stack
# =============================================================================


class Stack:
    def __init__(self):
        self._items: list = []

    def push(self, item) -> None:
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
    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"


# =============================================================================
# Practical: Balanced Parentheses
# =============================================================================


def is_balanced(expression: str) -> bool:
    """Use a stack to verify matching brackets — O(n) time."""
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
# Practical: Undo Stack
# =============================================================================


class TextEditor:
    def __init__(self):
        self._content = ""
        self._undo_stack = Stack()

    def type(self, text: str) -> None:
        self._undo_stack.push(self._content)
        self._content += text

    def undo(self) -> str:
        if not self._undo_stack.is_empty:
            self._content = self._undo_stack.pop()
        return self._content

    @property
    def content(self) -> str:
        return self._content


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Stack Operations ===")
    stack = Stack()
    for item in [1, 2, 3]:
        stack.push(item)
        print(f"  pushed {item}: {stack}")
    print(f"  peek: {stack.peek()}")
    print(f"  popped: {stack.pop()}")
    print(f"  after pop: {stack}")

    print("\n=== Balanced Parentheses ===")
    tests = ["(a + b) * [c]", "(a + b", "{[()]}", "([)]"]
    for expr in tests:
        print(f"  {expr!r:16} → {is_balanced(expr)}")

    print("\n=== Undo Stack ===")
    editor = TextEditor()
    editor.type("Hello")
    editor.type(" World")
    print(f"  content: {editor.content!r}")
    print(f"  undo:    {editor.undo()!r}")


if __name__ == "__main__":
    main()
