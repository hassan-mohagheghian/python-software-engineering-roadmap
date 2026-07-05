# Advanced - Packaging
# -----------------------------------------------------------------------------
# Packaging turns your code into a distributable project that others can
# install with pip. Modern Python uses pyproject.toml as the single
# configuration file.
#
# Key concepts:
# 1. pyproject.toml — project metadata, dependencies, build system.
# 2. uv — fast Python package manager (replaces pip + venv).
# 3. Entry points — CLI commands installed with the package.
# 4. Versioning — semantic versioning (major.minor.patch).
# -----------------------------------------------------------------------------


# =============================================================================
# pyproject.toml Structure
# =============================================================================


PYPROJECT_TOML = """
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-package"
version = "0.1.0"
description = "A short description"
readme = "README.md"
license = "MIT"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.28",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "mypy>=1.0",
]

[project.scripts]
my-cli = "my_package.cli:main"
""".strip()


# =============================================================================
# Project Layout
# =============================================================================


LAYOUT = """
my-package/
  pyproject.toml
  README.md
  src/
    my_package/
      __init__.py
      cli.py
      core.py
  tests/
    test_core.py
""".strip()


# =============================================================================
# uv Commands
# =============================================================================


UV_COMMANDS = """
# Create a new project
uv init my-package
cd my-package

# Add dependencies
uv add requests
uv add pytest --dev

# Run scripts in the project environment
uv run python -c "import my_package"

# Lock dependencies
uv lock

# Build the package
uv build

# Publish to PyPI
uv publish
""".strip()


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== pyproject.toml ===")
    print(PYPROJECT_TOML)

    print("\n=== Project Layout ===")
    print(LAYOUT)

    print("\n=== uv Commands ===")
    print(UV_COMMANDS)


if __name__ == "__main__":
    main()
