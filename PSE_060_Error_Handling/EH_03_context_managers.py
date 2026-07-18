# Error Handling - Context Managers
# -----------------------------------------------------------------------------
# Context managers ensure resources are properly acquired and released.
# The with statement guarantees cleanup even if errors occur.
#
# Key concepts:
# 1. __enter__ and __exit__ methods
# 2. @contextmanager decorator
# 3. Built-in context managers (open, lock)
# 4. Multiple context managers
# -----------------------------------------------------------------------------

import os
import threading
from contextlib import contextmanager

# =============================================================================
# Class-Based Context Manager
# =============================================================================


class Timer:
    """Measure execution time."""

    def __enter__(self):
        import time

        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time

        self.elapsed = time.time() - self.start
        print(f"  Elapsed: {self.elapsed:.4f}s")
        return False  # don't suppress exceptions


with Timer():
    import time

    time.sleep(0.1)


# =============================================================================
# @contextmanager Decorator
# =============================================================================


@contextmanager
def temp_directory():
    """Create and clean up a temporary directory."""
    import shutil
    import tempfile

    path = tempfile.mkdtemp()
    try:
        yield path
    finally:
        shutil.rmtree(path)


with temp_directory() as tmpdir:
    print(f"  Temp dir: {tmpdir}")


# =============================================================================
# Built-in Context Managers
# =============================================================================


# File handling
with open("test.txt", "w") as f:
    f.write("Hello, context managers!")

with open("test.txt") as f:
    print(f"  File content: {f.read()}")

# Threading lock

lock = threading.Lock()
with lock:
    print("  Lock acquired and released")


# =============================================================================
# Multiple Context Managers
# =============================================================================


with open("test.txt") as f:
    content = f.read()
    print(f"  Content: {content}")


# Nested syntax (Python 3.10+)
# with (open("a.txt") as a, open("b.txt") as b):
#     pass


# =============================================================================
# Practical: Database Connection
# =============================================================================


@contextmanager
def database_connection(url):
    """Simulate database connection management."""
    print(f"  Connecting to {url}")
    conn = {"url": url, "connected": True}
    try:
        yield conn
    finally:
        conn["connected"] = False
        print(f"  Disconnected from {url}")


with database_connection("postgres://localhost/mydb") as conn:
    print(f"  Connected: {conn['connected']}")


os.remove("test.txt")


def main():
    print("=== Context Managers ===")
    with Timer() as t:
        time.sleep(0.05)
    print(f"Timer elapsed: {t.elapsed:.4f}s")


if __name__ == "__main__":
    main()
