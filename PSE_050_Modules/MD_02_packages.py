# Modules - Packages
# -----------------------------------------------------------------------------
# Packages are directories containing Python modules and an optional __init__.py file.
# They allow organizing code into hierarchical namespaces.
#
# Key concepts:
# 1. __init__.py — marks directory as a regular package (optional since Python 3.3+)
# 2. Namespace packages — packages without __init__.py (Python 3.3+)
# 3. Subpackages
# 4. Relative imports
# 5. __all__ to control exports
# 6. __init__.py can execute initialization code
# -----------------------------------------------------------------------------


# =============================================================================
# Package Structure
# =============================================================================


"""
Regular Package (with __init__.py):
-----------------------------------
mypackage/
├── __init__.py        # marks it as a regular package (can contain code)
├── module_a.py
├── module_b.py
└── subpackage/
    ├── __init__.py
    └── module_c.py


Namespace Package (without __init__.py) - Python 3.3+:
-----------------------------------------------------
mynamespace/
├── module_a.py        # no __init__.py needed!
├── module_b.py
└── subpackage/
    └── module_c.py    # no __init__.py needed either!


Which to use?
-------------
- Regular package: when you need initialization code, __all__, or package-level variables
- Namespace package: when you want to split a package across multiple directories
- Recommendation: use __init__.py for most projects (better tooling support)
"""


# =============================================================================
# __init__.py — Regular Package Initialization
# =============================================================================

"""
# mypackage/__init__.py (Regular Package)

# Import symbols from submodules to expose them at package level
from .module_a import MyClass
from .module_b import helper_function

# Control what is exported with 'from package import *'
__all__ = ["MyClass", "helper_function", "VERSION"]

# Package-level variables and initialization code
VERSION = "1.0.0"

# Optional: run setup code when package is imported
def _initialize():
    print("Initializing mypackage...")

_initialize()
"""


# =============================================================================
# Namespace Packages — Python 3.3+ (No __init__.py)
# =============================================================================

"""
# Python 3.3 introduced PEP 420: Implicit Namespace Packages
# No __init__.py required, just create a directory with .py files.

mynamespace/
├── module_a.py        # works without __init__.py!
└── module_b.py

# This is useful when:
# - You want to split a package across multiple directories
# - You're creating a simple module collection without initialization
# - You're working with large projects where __init__.py overhead is unnecessary

# However, some tools (mypy, pylint) work better with regular packages.
"""


# =============================================================================
# Importing from Packages
# =============================================================================


"""
# Import entire module
import mypackage.module_a

# Import specific names
from mypackage import module_a
from mypackage.module_a import MyClass

# Import with alias
from mypackage import module_a as ma

# Import package itself (runs __init__.py if present)
import mypackage
print(mypackage.VERSION)        # if defined in __init__.py
print(mypackage.MyClass)        # if imported in __init__.py

# Namespace packages can be imported the same way
import mynamespace.module_a      # works without __init__.py!
"""


# =============================================================================
# Relative Imports
# =============================================================================


"""
# Inside a module within the package:

# From same package
from . import module_a
from .module_a import MyClass

# From parent package (one level up)
from .. import module_b

# From sibling subpackage
from ..subpackage import module_c

# Note: Relative imports only work inside a package.
# They cannot be used in the script being run directly (__name__ == "__main__").
"""


# =============================================================================
# __all__ Control
# =============================================================================


"""
# __init__.py — Regular Package
# mypackage/__init__.py
__all__ = ["MyClass", "VERSION"]  # Only these are exported with 'from package import *'

# Without __all__, 'from package import *' imports all public names
# (those whose names do not start with an underscore).
# """


# =============================================================================
# Package Best Practices (2026+)
# =============================================================================


"""
1. Always use __init__.py for packages you intend to share or publish.
   - Better compatibility with tools (mypy, pytest, IDE)
   - Allows initialization code
   - Exposes clean API via __all__

2. Use namespace packages (without __init__.py) only when:
   - You need to split a package across multiple directories
   - You're using Python 3.3+ and want minimal package structure

3. Avoid from package import * in production code.
   - It pollutes the namespace
   - Use explicit imports instead

4. Keep __init__.py minimal.
   - Import only what's needed for the public API
   - Avoid heavy computation or side effects
"""


def main():
    print("=== Packages in Modern Python (3.3+) ===")
    print("\nRegular packages:")
    print("  - Have __init__.py (optional but recommended)")
    print("  - Can run initialization code")
    print("  - Support __all__ and package-level variables")
    print("\nNamespace packages:")
    print("  - No __init__.py required (PEP 420)")
    print("  - Can split a package across multiple directories")
    print("  - Useful for plugin systems and large projects")
    print("\nRecommendation:")
    print("  - Use __init__.py for most projects")
    print("  - Use namespace packages only when you have a specific need")
    print("  - Relative imports use dot notation (from . import module)")
    print("  - Use __all__ to control exports")


if __name__ == "__main__":
    main()
