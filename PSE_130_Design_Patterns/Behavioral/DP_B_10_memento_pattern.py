# Design Patterns - Memento Pattern
# -------------------------------------------------------------------------
# The Memento Pattern captures and externalizes an object's internal state
# so it can be restored later, without violating encapsulation.
#
# The originator (the object whose state is saved) creates memento objects.
# A caretaker stores a history of mementos but never inspects their
# internals — only the originator knows how to save and restore.
#
# Benefits:
# - Undo / redo without exposing internal state
# - Snapshot-based state management (save points, transactions)
# - Clean separation between state owner and state storage
#
# Real-world examples:
# - Text editor undo / redo
# - Game save points and loading
# - Database transaction rollback
# - Version control (each commit is a memento of the repo state)
#
# Trade-offs:
# - Storing many snapshots can consume significant memory
# - Deep-copying large state is expensive
#
# Relationship to OOP Concepts:
#
# - Encapsulation:
#     The memento is opaque to the caretaker — only the originator
#     can read or write its contents.
#
# - Composition:
#     The caretaker holds references to memento objects.
#
# - Single Responsibility:
#     Originator owns state, caretaker owns history, memento owns snapshot.
#
# Relationship to SOLID:
#
# - SRP:
#     Each class has one job: save, store, or manage state.
#
# - OCP:
#     New stateful objects can adopt the pattern without changing
#     the caretaker.
# -------------------------------------------------------------------------


from __future__ import annotations

from typing import List

# =============================================================================
# Memento — the saved state (opaque to the caretaker)
# =============================================================================


class EditorMemento:
    """An immutable snapshot of the editor's state."""

    def __init__(self, text: str, cursor: int):
        self._text = text
        self._cursor = cursor

    @property
    def text(self) -> str:
        return self._text

    @property
    def cursor(self) -> int:
        return self._cursor


# =============================================================================
# Originator — the object whose state is saved / restored
# =============================================================================


class Editor:
    """A simple text editor that can save and restore snapshots."""

    def __init__(self):
        self._text = ""
        self._cursor = 0

    def type(self, words: str):
        self._text = self._text[: self._cursor] + words + self._text[self._cursor :]
        self._cursor += len(words)

    def move_cursor(self, position: int):
        self._cursor = max(0, min(position, len(self._text)))

    def save(self) -> EditorMemento:
        return EditorMemento(self._text, self._cursor)

    def restore(self, memento: EditorMemento):
        self._text = memento.text
        self._cursor = memento.cursor

    def __str__(self):
        return f'"{self._text}" (cursor={self._cursor})'


# =============================================================================
# Caretaker — stores history, never inspects memento internals
# =============================================================================


class History:
    """Maintains an undo/redo stack of mementos."""

    def __init__(self):
        self._undo_stack: List[EditorMemento] = []
        self._redo_stack: List[EditorMemento] = []

    def push(self, memento: EditorMemento):
        self._undo_stack.append(memento)
        self._redo_stack.clear()

    def undo(self) -> EditorMemento | None:
        if not self._undo_stack:
            return None
        memento = self._undo_stack.pop()
        self._redo_stack.append(memento)
        # Return the previous state (one before the popped one)
        if self._undo_stack:
            return self._undo_stack[-1]
        return EditorMemento("", 0)

    def redo(self) -> EditorMemento | None:
        if not self._redo_stack:
            return None
        memento = self._redo_stack.pop()
        self._undo_stack.append(memento)
        return memento

    @property
    def can_undo(self) -> bool:
        return len(self._undo_stack) > 1

    @property
    def can_redo(self) -> bool:
        return len(self._redo_stack) > 0


# =============================================================================
# Usage
# =============================================================================


def main():
    editor = Editor()
    history = History()

    # Type some text, saving after each action
    editor.type("Hello")
    history.push(editor.save())
    print(f"After typing 'Hello': {editor}")

    editor.type(" World")
    history.push(editor.save())
    print(f"After typing ' World': {editor}")

    editor.type("!")
    history.push(editor.save())
    print(f"After typing '!':     {editor}")

    # Undo twice
    print("\n=== Undo ===")
    state = history.undo()
    if state:
        editor.restore(state)
    print(f"Undo 1: {editor}")

    state = history.undo()
    if state:
        editor.restore(state)
    print(f"Undo 2: {editor}")

    # Redo once
    print("\n=== Redo ===")
    state = history.redo()
    if state:
        editor.restore(state)
    print(f"Redo 1: {editor}")


if __name__ == "__main__":
    main()
