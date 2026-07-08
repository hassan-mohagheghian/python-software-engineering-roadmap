# Functions - *args and **kwargs
# -----------------------------------------------------------------------------
# *args and **kwargs allow functions to accept a variable number of arguments.
# This makes functions more flexible and reusable.
#
# Key concepts:
# 1. *args — collects extra positional arguments as a tuple
# 2. **kwargs — collects extra keyword arguments as a dict
# 3. Unpacking with * and **
# 4. Order: positional, *args, keyword, **kwargs
# -----------------------------------------------------------------------------


# =============================================================================
# *args Basics
# =============================================================================


def add_all(*args):
    """Sum any number of arguments."""
    print(f"  args = {args}")
    return sum(args)


print(f"Sum: {add_all(1, 2, 3)}")
print(f"Sum: {add_all(10, 20, 30, 40)}")


# =============================================================================
# **kwargs Basics
# =============================================================================


def print_config(**kwargs):
    """Print all configuration key-value pairs."""
    for key, value in kwargs.items():
        print(f"    {key} = {value}")


print_config(host="localhost", port=8080, debug=True)


# =============================================================================
# Combining *args and **kwargs
# =============================================================================


def log(level, *messages, **options):
    """Log messages with a level and optional settings."""
    print(f"[{level}] {' '.join(messages)}")
    if options:
        print(f"  Options: {options}")


log("INFO", "Server started", "on port 8080")
log("ERROR", "Connection failed", retry=3, timeout=30)


# =============================================================================
# Unpacking with * and **
# =============================================================================


def greet(first, last, greeting="Hello"):
    """Greet someone."""
    return f"{greeting}, {first} {last}!"


args = ("Alice", "Smith")
kwargs = {"greeting": "Hi"}
print(greet(*args, **kwargs))


# =============================================================================
# Keyword-Only Arguments
# =============================================================================


def create_user(name, *, email, role="user"):
    """Create user — email and role are keyword-only (after *)."""
    return f"{name} ({email}) [{role}]"


print(create_user("Alice", email="alice@example.com", role="admin"))


def main():
    print("=== *args and **kwargs ===")
    print(f"Add: {add_all(1, 2, 3, 4)}")
    print_config(name="test", verbose=True)
    log("WARN", "Disk space low", disk="/dev/sda1")


if __name__ == "__main__":
    main()
