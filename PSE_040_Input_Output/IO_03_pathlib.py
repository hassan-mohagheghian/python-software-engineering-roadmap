# Input/Output - pathlib
# -----------------------------------------------------------------------------
# pathlib provides an object-oriented way to work with file system paths.
# It is the modern replacement for os.path.
#
# Key concepts:
# 1. Path object creation
# 2. Path properties (name, stem, suffix, parent)
# 3. Path operations (join, resolve, exists)
# 4. Reading and writing files
# 5. Globbing and iterating directories
# -----------------------------------------------------------------------------


# =============================================================================
# Creating Paths
# =============================================================================


from pathlib import Path

# From string
p = Path("/home/user/documents/file.txt")
print(f"Path: {p}")
print(f"  Name: {p.name}")
print(f"  Stem: {p.stem}")
print(f"  Suffix: {p.suffix}")
print(f"  Parent: {p.parent}")

# Current directory
cwd = Path.cwd()
print(f"CWD: {cwd}")

# Home directory
home = Path.home()
print(f"Home: {home}")


# =============================================================================
# Path Operations
# =============================================================================


# Joining paths
base = Path("/home/user")
full = base / "documents" / "file.txt"
print(f"Joined: {full}")

# Resolve absolute path
relative = Path("./some/file.txt")
print(f"Resolved: {relative.resolve()}")


# =============================================================================
# Checking Existence
# =============================================================================


test_path = Path("test_file.txt")
print(f"Exists: {test_path.exists()}")
print(f"Is file: {test_path.is_file()}")
print(f"Is dir: {test_path.is_dir()}")


# =============================================================================
# Reading and Writing
# =============================================================================


# Write text
output = Path("output.txt")
output.write_text("Hello, pathlib!")
print(f"Read: {output.read_text()}")

# Write bytes
binary = Path("data.bin")
binary.write_bytes(b"\x00\x01\x02")

# Cleanup
output.unlink(missing_ok=True)
binary.unlink(missing_ok=True)


# =============================================================================
# Globbing
# =============================================================================


# Find all .py files
py_files = list(Path(".").glob("*.py"))
print(f"Python files: {len(py_files)}")

# Recursive glob
all_files = list(Path(".").rglob("*.py"))
print(f"All Python files: {len(all_files)}")


def main():
    print("=== pathlib ===")
    p = Path("test_dir")
    p.mkdir(exist_ok=True)
    (p / "file.txt").write_text("test content")
    print(f"Files: {list(p.iterdir())}")
    (p / "file.txt").unlink()
    p.rmdir()


if __name__ == "__main__":
    main()
