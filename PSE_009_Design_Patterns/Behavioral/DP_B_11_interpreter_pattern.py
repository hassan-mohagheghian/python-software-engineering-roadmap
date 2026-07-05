# Design Patterns - Interpreter Pattern
# -------------------------------------------------------------------------
# The Interpreter Pattern defines a grammar for a language and provides
# an interpreter that uses this grammar to evaluate sentences in the
# language.
#
# Each rule in the grammar is represented by a class. An expression tree
# is built from these classes, and calling interpret() on the root node
# evaluates the whole expression.
#
# Benefits:
# - Each grammar rule is a clean, self-contained class (SRP)
# - Easy to add new rules without changing existing ones (OCP)
# - The grammar is expressed directly in code — no parser library needed
#
# Real-world examples:
# - SQL query interpreters
# - Mathematical expression evaluators
# - Regular expression engines
# - Configuration file parsers (e.g. simple DSLs)
# - Template languages (Handlebars, Jinja2)
#
# Trade-offs:
# - Complex grammars lead to many classes
# - Not efficient for large or frequently evaluated expressions
# - For complex languages, a parser generator (ANTLR, PLY) is better
#
# Relationship to OOP Concepts:
#
# - Polymorphism:
#     Every expression type implements interpret() differently but
#     shares the same interface.
#
# - Composite:
#     Expressions are composed into a tree structure. An Add node
#     contains two child expressions.
#
# - Recursion:
#     interpret() calls interpret() on children, walking the tree.
#
# Relationship to SOLID:
#
# - SRP:
#     Each class represents exactly one grammar rule.
#
# - OCP:
#     New operators are added by creating new classes, not by
#     modifying existing ones.
#
# - LSP:
#     Any expression can be used wherever an Expression is expected.
# -------------------------------------------------------------------------


from abc import ABC, abstractmethod


# =============================================================================
# Expression Interface
# =============================================================================


class Expression(ABC):
    """Every grammar rule must implement interpret()."""

    @abstractmethod
    def interpret(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


# =============================================================================
# Terminal Expressions (leaf nodes)
# =============================================================================


class Number(Expression):
    """A literal numeric value."""

    def __init__(self, value: float):
        self.value = value

    def interpret(self) -> float:
        return self.value

    def __str__(self) -> str:
        return str(self.value)


# =============================================================================
# Non-Terminal Expressions (operator nodes)
# =============================================================================


class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() + self.right.interpret()

    def __str__(self) -> str:
        return f"({self.left} + {self.right})"


class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() - self.right.interpret()

    def __str__(self) -> str:
        return f"({self.left} - {self.right})"


class Multiply(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        return self.left.interpret() * self.right.interpret()

    def __str__(self) -> str:
        return f"({self.left} * {self.right})"


class Divide(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> float:
        divisor = self.right.interpret()
        if divisor == 0:
            raise ValueError("Division by zero")
        return self.left.interpret() / divisor

    def __str__(self) -> str:
        return f"({self.left} / {self.right})"


# =============================================================================
# Usage
# =============================================================================


def main():
    # Build expression trees manually (no parser needed)

    # (3 + 5) => 8
    expr1 = Add(Number(3), Number(5))
    print(f"{expr1} = {expr1.interpret()}")

    # (10 - 2) => 8
    expr2 = Subtract(Number(10), Number(2))
    print(f"{expr2} = {expr2.interpret()}")

    # (4 * 3) => 12
    expr3 = Multiply(Number(4), Number(3))
    print(f"{expr3} = {expr3.interpret()}")

    # (20 / 4) => 5
    expr4 = Divide(Number(20), Number(4))
    print(f"{expr4} = {expr4.interpret()}")

    # Complex: ((3 + 5) * (10 - 2)) => 64
    complex_expr = Multiply(
        Add(Number(3), Number(5)),
        Subtract(Number(10), Number(2)),
    )
    print(f"\n{complex_expr} = {complex_expr.interpret()}")

    # Complex: ((100 - 10) / (3 * 3)) => 10
    complex_expr2 = Divide(
        Subtract(Number(100), Number(10)),
        Multiply(Number(3), Number(3)),
    )
    print(f"{complex_expr2} = {complex_expr2.interpret()}")


if __name__ == "__main__":
    main()
