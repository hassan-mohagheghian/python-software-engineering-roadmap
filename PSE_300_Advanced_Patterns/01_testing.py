# Advanced - Testing with unittest and pytest
# -----------------------------------------------------------------------------
# Testing verifies that code works correctly. Python ships with unittest;
# pytest is a popular third-party framework with simpler syntax.
#
# Key concepts:
# 1. unittest — TestCase, assert methods, setUp/tearDown.
# 2. pytest — simpler assertions, fixtures, parametrize.
# 3. Test organization — one test per behavior, clear naming.
# 4. Coverage — which lines of code are exercised by tests.
# -----------------------------------------------------------------------------


import unittest


# =============================================================================
# Code Under Test
# =============================================================================


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# =============================================================================
# unittest Tests
# =============================================================================


class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


class TestDivide(unittest.TestCase):
    def test_normal(self):
        self.assertAlmostEqual(divide(10, 2), 5.0)

    def test_float(self):
        self.assertAlmostEqual(divide(1, 3), 0.333, places=3)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_with_spaces(self):
        self.assertTrue(is_palindrome("race car"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))


# =============================================================================
# pytest-style Tests (run with: pytest 01_testing.py -v)
# =============================================================================


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    try:
        divide(1, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False


# =============================================================================
# Usage
# =============================================================================


if __name__ == "__main__":
    unittest.main()
