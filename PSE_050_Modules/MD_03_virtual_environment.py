# Modules - Virtual Environment
# -----------------------------------------------------------------------------
# A virtual environment is an isolated Python installation for a project.
# It prevents dependency conflicts between projects.
#
# Key concepts:
# 1. venv — built-in virtual environment module
# 2. Creating and activating environments
# 3. Installing packages with pip
# 4. pyproject.toml — modern project configuration
# -----------------------------------------------------------------------------


# =============================================================================
# Creating a Virtual Environment
# =============================================================================


"""
# Create virtual environment
python -m venv .venv

# Activate (Linux/Mac)
source .venv/bin/activate

# Activate (Windows)
.venv\\Scripts\\activate

# Deactivate
deactivate
"""


# =============================================================================
# Installing Packages
# =============================================================================

"""
# Install a package
pip install requests

# Install specific version
pip install requests==2.31.0

# Install from requirements file
pip install -r requirements.txt

# Save dependencies
pip freeze > requirements.txt
"""


# =============================================================================
# pyproject.toml (Modern Standard)
# =============================================================================


"""
[project]
name = "my-project"
version = "0.1.0"
description = "A sample project"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28",
    "click>=8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.1",
]

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.backends._legacy:_Backend"
"""


# =============================================================================
# uv — Fast Package Manager
# =============================================================================


"""
# Install uv
pip install uv

# Create venv
uv venv

# Add dependency
uv add requests

# Sync from lock file
uv sync
"""


def main():
    print("=== Virtual Environment ===")
    print("1. Create: python -m venv .venv")
    print("2. Activate: source .venv/bin/activate")
    print("3. Install: pip install <package>")
    print("4. Save: pip freeze > requirements.txt")


if __name__ == "__main__":
    main()
