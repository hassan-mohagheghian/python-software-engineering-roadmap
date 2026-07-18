# Modules - Dependency Management
# -----------------------------------------------------------------------------
# Managing project dependencies ensures reproducible environments.
# Modern Python uses pyproject.toml with tools like pip, uv, or poetry.
#
# Key concepts:
# 1. requirements.txt — pinned versions
# 2. pyproject.toml — project metadata + dependencies
# 3. Lock files — exact resolved versions
# 4. Virtual environments — isolation
# -----------------------------------------------------------------------------


# =============================================================================
# requirements.txt
# =============================================================================


"""
# Direct dependencies
requests==2.31.0
click>=8.0,<9.0
flask~=2.3

# From git
git+https://github.com/user/repo@main

# Editable install
-e ./local-package
"""


# =============================================================================
# pyproject.toml Dependencies
# =============================================================================


"""
[project]
dependencies = [
    "requests>=2.28",
    "click>=8.0",
]

[project.optional-dependencies]
test = ["pytest>=7.0"]
lint = ["ruff>=0.1"]
"""


# =============================================================================
# Lock Files
# =============================================================================


"""
# uv.lock (auto-generated, commit this)
# Ensures everyone gets the exact same versions

# poetry.lock (similar concept)

# Generate lock file
uv lock
poetry lock
"""


# =============================================================================
# Installing from Lock
# =============================================================================


"""
# Install exact versions from lock
uv sync

# Install with extras
uv sync --extra test

# Install production only (no dev deps)
uv sync --no-dev
"""


# =============================================================================
# Version Specifiers
# =============================================================================


"""
# Exact version
requests==2.31.0

# Minimum version
requests>=2.28

# Compatible release
requests~=2.31    # >=2.31.0, <2.32.0

# Range
requests>=2.28,<3.0
"""


def main():
    print("=== Dependency Management ===")
    print("1. Define deps in pyproject.toml")
    print("2. Lock with: uv lock")
    print("3. Install with: uv sync")
    print("4. Add new: uv add <package>")


if __name__ == "__main__":
    main()
