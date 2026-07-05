# Advanced - Type Checking
# -----------------------------------------------------------------------------
# Type hints make Python code self-documenting and catch errors before
# runtime. Tools like mypy check types statically.
#
# Key concepts:
# 1. Basic hints — int, str, float, bool, None.
# 2. Collections — list[int], dict[str, int], tuple[int, ...].
# 3. Union / Optional — int | None, str | int.
# 4. Protocol — structural subtyping (duck typing with types).
# 5. Generics — TypeVar for reusable type-safe containers.
# -----------------------------------------------------------------------------


from typing import Protocol


# =============================================================================
# Basic Type Hints
# =============================================================================


def greet(name: str) -> str:
    return f"Hello, {name}!"


def area(width: float, height: float) -> float:
    return width * height


# =============================================================================
# Collections
# =============================================================================


def sum_list(numbers: list[int]) -> int:
    return sum(numbers)


def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


# =============================================================================
# Union and Optional
# =============================================================================


def find_first(items: list[str], target: str) -> str | None:
    for item in items:
        if item == target:
            return item
    return None


# =============================================================================
# Protocol — Structural Subtyping
# =============================================================================


class Drawable(Protocol):
    def draw(self) -> str: ...


class Circle:
    def draw(self) -> str:
        return "Drawing circle"


class Square:
    def draw(self) -> str:
        return "Drawing square"


def render(shape: Drawable) -> str:
    return shape.draw()


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Basic Hints ===")
    print(f"  greet('Alice'): {greet('Alice')}")
    print(f"  area(4, 5): {area(4, 5)}")

    print("\n=== Collections ===")
    print(f"  sum_list: {sum_list([1, 2, 3, 4])}")
    print(f"  word_count: {word_count('a b a c b a')}")

    print("\n=== Optional ===")
    result = find_first(["x", "y", "z"], "y")
    print(f"  find_first 'y': {result}")
    result = find_first(["x", "y", "z"], "w")
    print(f"  find_first 'w': {result}")

    print("\n=== Protocol ===")
    print(f"  render(Circle): {render(Circle())}")
    print(f"  render(Square): {render(Square())}")


if __name__ == "__main__":
    main()
