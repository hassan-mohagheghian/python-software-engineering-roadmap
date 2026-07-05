# Design Patterns - Command Pattern
# -----------------------------------------------------------------------------
# The Command Pattern is a behavioral design pattern that turns a request into
# a stand-alone object containing all information about the request.
#
# This lets you parameterize methods with different requests, delay or queue a
# request's execution, and support undoable operations.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - You want to decouple the object that invokes the operation from the one
#   that knows how to perform it.
# - You want to queue, log, or undo operations.
# - You need to assemble a set of operations from simpler building blocks.
#
# -----------------------------------------------------------------------------
# Key Idea:
#
#   Invoker -> Command -> Receiver
#
#   The invoker holds a command object and calls execute().
#   The command knows which receiver to call and with what arguments.
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Decouples sender from receiver.
# - Commands are first-class objects (can be stored, passed, logged).
# - Easy to implement undo/redo.
# - Follows Single Responsibility Principle (SRP).
# - Follows Open/Closed Principle (OCP).
#
# -----------------------------------------------------------------------------
# Example:
#
# A text editor where each action (type, delete, move cursor) is a command.
# Commands support undo so the user can reverse any action.
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# Receiver - the object that does the actual work
# -----------------------------------------------------------------------------


class TextEditor:
    def __init__(self):
        self.content: list[str] = []
        self.cursor: int = 0

    def insert(self, text: str):
        for char in text:
            self.content.insert(self.cursor, char)
            self.cursor += 1

    def delete(self, count: int) -> str:
        deleted = ""
        for _ in range(count):
            if self.cursor < len(self.content):
                deleted += self.content.pop(self.cursor)
        return deleted

    def move_cursor(self, position: int) -> int:
        old = self.cursor
        self.cursor = max(0, min(position, len(self.content)))
        return old

    def get_text(self) -> str:
        return "".join(self.content)


# -----------------------------------------------------------------------------
# Command (Abstract)
# -----------------------------------------------------------------------------


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# -----------------------------------------------------------------------------
# Concrete Commands
# -----------------------------------------------------------------------------


class InsertCommand(Command):
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.insert(self.text)

    def undo(self):
        self.editor.cursor -= len(self.text)
        self.editor.delete(len(self.text))


class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, count: int):
        self.editor = editor
        self.count = count
        self.deleted: str = ""

    def execute(self):
        self.deleted = self.editor.delete(self.count)

    def undo(self):
        self.editor.insert(self.deleted)


class MoveCursorCommand(Command):
    def __init__(self, editor: TextEditor, position: int):
        self.editor = editor
        self.position = position
        self.old_position: int = 0

    def execute(self):
        self.old_position = self.editor.move_cursor(self.position)

    def undo(self):
        self.editor.move_cursor(self.old_position)


# -----------------------------------------------------------------------------
# Invoker - manages command execution and history
# -----------------------------------------------------------------------------


class CommandHistory:
    def __init__(self):
        self._history: list[Command] = []
        self._redo_stack: list[Command] = []

    def execute(self, command: Command):
        command.execute()
        self._history.append(command)
        self._redo_stack.clear()

    def undo(self):
        if self._history:
            command = self._history.pop()
            command.undo()
            self._redo_stack.append(command)
        else:
            print("  Nothing to undo")

    def redo(self):
        if self._redo_stack:
            command = self._redo_stack.pop()
            command.execute()
            self._history.append(command)
        else:
            print("  Nothing to redo")


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    editor = TextEditor()
    history = CommandHistory()

    # Type "Hello"
    history.execute(InsertCommand(editor, "Hello"))
    print(f"After 'Hello':       '{editor.get_text()}' (cursor: {editor.cursor})")

    # Type " World"
    history.execute(InsertCommand(editor, " World"))
    print(f"After ' World':      '{editor.get_text()}' (cursor: {editor.cursor})")

    # Type "!"
    history.execute(InsertCommand(editor, "!"))
    print(f"After '!':           '{editor.get_text()}' (cursor: {editor.cursor})")

    # Undo "!"
    history.undo()
    print(f"After undo:          '{editor.get_text()}' (cursor: {editor.cursor})")

    # Undo " World"
    history.undo()
    print(f"After undo:          '{editor.get_text()}' (cursor: {editor.cursor})")

    # Redo " World"
    history.redo()
    print(f"After redo:          '{editor.get_text()}' (cursor: {editor.cursor})")

    # Move cursor to start and insert "Say "
    history.execute(MoveCursorCommand(editor, 0))
    history.execute(InsertCommand(editor, "Say "))
    print(f"After insert at 0:   '{editor.get_text()}' (cursor: {editor.cursor})")

    # Delete "Say "
    history.execute(DeleteCommand(editor, 4))
    print(f"After delete 4:      '{editor.get_text()}' (cursor: {editor.cursor})")

    # Undo delete
    history.undo()
    print(f"After undo:          '{editor.get_text()}' (cursor: {editor.cursor})")


if __name__ == "__main__":
    main()
