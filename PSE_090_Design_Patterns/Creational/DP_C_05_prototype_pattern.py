# Design Patterns - Prototype Pattern
# -----------------------------------------------------------------------------
# The Prototype Pattern is a creational design pattern that lets you copy
# existing objects without making your code dependent on their classes.
#
# Instead of creating new objects from scratch, you clone an existing
# instance (the prototype) and modify the copy as needed.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - Object creation is expensive (database calls, network, complex setup).
# - You need many similar objects with slight variations.
# - You want to avoid subclasses just to create configured variants.
# - You need to snapshot and restore object state.
#
# -----------------------------------------------------------------------------
# Key Idea:
#
#   Prototype (interface) -> clone()
#   ConcretePrototype     -> clone() returns a copy of itself
#
#   Client calls prototype.clone() instead of new ConcretePrototype()
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Avoids costly initialization.
# - Reduces the need for subclasses.
# - Simplifies creation of complex objects.
# - Python's copy module makes this natural.
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Cloning game characters with base stats.
# - Duplicating document templates.
# - Copying configuration objects for per-request overrides.
# - Caching pre-built UI components.
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod
import copy


# -----------------------------------------------------------------------------
# Prototype Interface
# -----------------------------------------------------------------------------


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype":
        pass


# -----------------------------------------------------------------------------
# Concrete Prototype
# -----------------------------------------------------------------------------


class Enemy(Prototype):
    def __init__(self, name: str, health: int, attack: int, abilities: list[str]):
        self.name = name
        self.health = health
        self.attack = attack
        self.abilities = abilities

    def clone(self) -> "Enemy":
        return copy.deepcopy(self)

    def __str__(self):
        return (
            f"Enemy(name={self.name}, "
            f"health={self.health}, "
            f"attack={self.attack}, "
            f"abilities={self.abilities})"
        )


# -----------------------------------------------------------------------------
# Prototype Registry (optional)
# -----------------------------------------------------------------------------


class EnemyRegistry:
    """Stores pre-configured prototypes for quick cloning."""

    def __init__(self):
        self._prototypes: dict[str, Enemy] = {}

    def register(self, key: str, prototype: Enemy):
        self._prototypes[key] = prototype

    def create(self, key: str, **overrides) -> Enemy:
        prototype = self._prototypes[key]
        clone = prototype.clone()
        for attr, value in overrides.items():
            setattr(clone, attr, value)
        return clone


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    # Create base prototypes
    registry = EnemyRegistry()

    registry.register(
        "goblin",
        Enemy(name="Goblin", health=50, attack=8, abilities=["stab", "dodge"]),
    )
    registry.register(
        "dragon",
        Enemy(
            name="Dragon",
            health=500,
            attack=50,
            abilities=["fire_breath", "tail_swipe", "fly"],
        ),
    )

    # Clone and customize
    goblin1 = registry.create("goblin")
    goblin2 = registry.create("goblin", name="Goblin Chief", health=80, attack=15)

    dragon1 = registry.create("dragon")
    dragon2 = registry.create("dragon", name="Elder Dragon", health=800)

    print("--- Cloned Enemies ---")
    print(goblin1)
    print(goblin2)
    print(dragon1)
    print(dragon2)

    # Verify deep copy (modifying clone does not affect original)
    goblin2.abilities.append("summon_wolf")
    print("\n--- After modifying goblin2 ---")
    print(f"Original abilities: {goblin1.abilities}")
    print(f"Clone abilities:    {goblin2.abilities}")


if __name__ == "__main__":
    main()
