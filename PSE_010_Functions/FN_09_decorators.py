# Functions - Decorators
# -----------------------------------------------------------------------------
# Decorators modify or extend function behavior without changing the
# function's source code. They use the @decorator syntax and are
# widely used in Python frameworks.
#
# Key concepts:
# 1. @decorator syntax
# 2. Wrapping functions
# 3. functools.wraps for preserving metadata
# 4. Parameterized decorators
# 5. Stacking decorators
# -----------------------------------------------------------------------------

import functools

# =============================================================================
# Basic Decorator
# =============================================================================


def timer(func):
    """Measure function execution time.

    NOTE: Without @functools.wraps, func.__name__ and __doc__ are lost
    and become 'wrapper' instead. Always use functools.wraps (see below).
    """
    import time

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  {func.__name__} took {elapsed:.4f}s")
        return result

    return wrapper


@timer
def slow_function():
    """Simulate slow work."""
    import time

    time.sleep(0.1)
    return "done"


slow_function()


# =============================================================================
# Why functools.wraps is Required (Not Optional)
# =============================================================================
# Without @functools.wraps(func) on the inner wrapper, the decorated function
# loses its __name__, __doc__, __module__, and __wrapped__ attributes. This
# breaks introspection, help(), debugging, and any library that relies on
# function metadata.
#
# ALWAYS use @functools.wraps(func) on every inner wrapper function. There
# is no reason to skip it — it has zero cost and prevents subtle bugs.
# =============================================================================


def log_calls(func):
    """Log every function call."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__}{args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned {result}")
        return result

    return wrapper


@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b


add(3, 5)
print(f"  Function name: {add.__name__}")  # preserved by wraps


# =============================================================================
# Parameterized Decorator
# =============================================================================


def repeat(times):
    """Repeat a function call N times."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator


@repeat(times=3)
def say_hello():
    return "hello"


print(f"  repeat: {say_hello()}")


# =============================================================================
# Stacking Decorators
# =============================================================================
# Stacked decorators execute in REVERSE order — the bottom-most decorator
# (closest to the function) runs first, and the top-most runs last.
#
# @bold        <-- runs 3rd (outermost)
# @italic      <-- runs 2nd
# def greet(): <-- runs 1st (innermost)
#
# Equivalent to: bold(italic(greet))
# =============================================================================


def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"

    return wrapper


def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"*{func(*args, **kwargs)}*"

    return wrapper


@bold
@italic
def greet(name):
    return f"Hello, {name}"


print(f"  Stacked: {greet('World')}")


def main():
    print("=== Decorators ===")
    slow_function()
    print(f"Add: {add(10, 20)}")
    print(f"Repeat: {say_hello()}")
    print(f"Stacked: {greet('Python')}")


if __name__ == "__main__":
    main()
