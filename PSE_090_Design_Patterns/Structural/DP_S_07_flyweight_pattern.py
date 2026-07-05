# Design Patterns - Flyweight Pattern
# -----------------------------------------------------------------------------
# The Flyweight Pattern is a structural design pattern that reduces memory usage
# by sharing common object data instead of storing duplicate copies everywhere.
#
# It separates object state into two parts:
#
# - Intrinsic state: shared data stored inside the flyweight object.
# - Extrinsic state: unique data passed from the outside when needed.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - You need to create many similar objects.
# - Many objects repeat the same data.
# - Memory usage matters.
# - Shared data can be made immutable.
#
# -----------------------------------------------------------------------------
# Key Idea:
#
# Client -> Flyweight Factory -> Shared Flyweight
#
# The factory returns an existing object when the same shared state is requested.
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Reduces memory usage.
# - Avoids duplicate objects.
# - Keeps shared state centralized.
# - Works well for text editors, games, icons, particles, and map markers.
#
# -----------------------------------------------------------------------------
# Example:
#
# A text editor can contain thousands of characters. Each character has unique
# data like the letter and position, but many characters share the same style
# such as font family, font size, and color.
# -----------------------------------------------------------------------------

from dataclasses import dataclass

# -----------------------------------------------------------------------------
# Flyweight
# -----------------------------------------------------------------------------


@dataclass(frozen=True)
class CharacterStyle:
    font_family: str
    font_size: int
    color: str

    def render(self, character: str, line: int, column: int):
        print(
            f"'{character}' at ({line}, {column}) | "
            f"{self.font_family}, {self.font_size}px, {self.color}"
        )


# -----------------------------------------------------------------------------
# Flyweight Factory
# -----------------------------------------------------------------------------


class CharacterStyleFactory:
    def __init__(self):
        self._styles: dict[tuple[str, int, str], CharacterStyle] = {}

    def get_style(self, font_family: str, font_size: int, color: str) -> CharacterStyle:
        key = (font_family, font_size, color)

        if key not in self._styles:
            print(f"[FACTORY] Creating new style: {key}")
            self._styles[key] = CharacterStyle(font_family, font_size, color)
        else:
            print(f"[FACTORY] Reusing existing style: {key}")

        return self._styles[key]

    def total_styles(self) -> int:
        return len(self._styles)


# -----------------------------------------------------------------------------
# Context Object
# -----------------------------------------------------------------------------


@dataclass
class TextCharacter:
    character: str
    line: int
    column: int
    style: CharacterStyle

    def render(self):
        self.style.render(self.character, self.line, self.column)


# -----------------------------------------------------------------------------
# Client
# -----------------------------------------------------------------------------


class TextDocument:
    def __init__(self, style_factory: CharacterStyleFactory):
        self._style_factory = style_factory
        self._characters: list[TextCharacter] = []

    def add_character(
        self,
        character: str,
        line: int,
        column: int,
        font_family: str,
        font_size: int,
        color: str,
    ):
        style = self._style_factory.get_style(font_family, font_size, color)
        self._characters.append(TextCharacter(character, line, column, style))

    def render(self):
        for character in self._characters:
            character.render()


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    style_factory = CharacterStyleFactory()
    document = TextDocument(style_factory)

    document.add_character("H", 1, 1, "Arial", 14, "black")
    document.add_character("e", 1, 2, "Arial", 14, "black")
    document.add_character("l", 1, 3, "Arial", 14, "black")
    document.add_character("l", 1, 4, "Arial", 14, "black")
    document.add_character("o", 1, 5, "Arial", 14, "black")

    document.add_character("!", 1, 6, "Arial", 14, "red")

    print("\n===== Render Document =====")
    document.render()

    print("\n===== Shared Flyweights =====")
    print("Characters created: 6")
    print(f"Style objects created: {style_factory.total_styles()}")


if __name__ == "__main__":
    main()
