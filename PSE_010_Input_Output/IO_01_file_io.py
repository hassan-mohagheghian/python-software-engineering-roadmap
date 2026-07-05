# Python Basics - File I/O
# -----------------------------------------------------------------------------
# File I/O allows reading from and writing to files on disk.
#
# Key concepts:
# 1. Opening files — open(), modes (r, w, a, rb, wb).
# 2. Context managers — with statement for safe file handling.
# 3. Reading — read(), readline(), readlines(), iteration.
# 4. Writing — write(), writelines().
# 5. CSV and JSON — common file formats.
# 6. Path handling — pathlib module.
# -----------------------------------------------------------------------------


# =============================================================================
# Writing Files
# =============================================================================


# Write a text file
def write_sample_file():
    with open("sample.txt", "w") as f:
        f.write("Hello, World!\n")
        f.write("Second line\n")
        f.write("Third line\n")
    print("Wrote sample.txt")


# Append to a file
def append_to_file():
    with open("sample.txt", "a") as f:
        f.write("Appended line\n")
    print("Appended to sample.txt")


# =============================================================================
# Reading Files
# =============================================================================


# Read entire file
def read_entire_file():
    with open("sample.txt", "r") as f:
        content = f.read()
    print(f"Full content:\n{content}")


# Read line by line
def read_line_by_line():
    with open("sample.txt", "r") as f:
        for line in f:
            print(f"  Line: {line.strip()}")


# Read into list
def read_as_list():
    with open("sample.txt", "r") as f:
        lines = f.readlines()
    print(f"Lines list: {[l.strip() for l in lines]}")


# =============================================================================
# Binary Files
# =============================================================================


def write_binary():
    data = bytes([72, 101, 108, 108, 111])  # "Hello"
    with open("sample.bin", "wb") as f:
        f.write(data)
    print("Wrote sample.bin")


def read_binary():
    with open("sample.bin", "rb") as f:
        data = f.read()
    print(f"Binary content: {data}")
    print(f"As string: {data.decode()}")


# =============================================================================
# CSV Files
# =============================================================================


import csv


def write_csv():
    rows = [
        ["name", "age", "city"],
        ["Alice", 30, "NYC"],
        ["Bob", 25, "LA"],
        ["Charlie", 35, "Chicago"],
    ]
    with open("sample.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Wrote sample.csv")


def read_csv():
    with open("sample.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"  {row}")


# =============================================================================
# JSON Files
# =============================================================================


import json


def write_json():
    data = {
        "users": [
            {"name": "Alice", "age": 30, "active": True},
            {"name": "Bob", "age": 25, "active": False},
        ],
        "count": 2
    }
    with open("sample.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Wrote sample.json")


def read_json():
    with open("sample.json", "r") as f:
        data = json.load(f)
    print(f"JSON data: {data}")
    print(f"Users: {data['users']}")


# =============================================================================
# Pathlib (Modern Path Handling)
# =============================================================================


from pathlib import Path


def pathlib_demo():
    # Create path
    p = Path("demo_dir")

    # Create directory
    p.mkdir(exist_ok=True)
    print(f"Created dir: {p}")

    # Write file
    (p / "test.txt").write_text("Hello from pathlib!")
    print(f"Wrote: {p / 'test.txt'}")

    # Read file
    content = (p / "test.txt").read_text()
    print(f"Content: {content}")

    # List directory
    print(f"Contents: {list(p.iterdir())}")

    # Path properties
    file_path = p / "test.txt"
    print(f"Name: {file_path.name}")
    print(f"Stem: {file_path.stem}")
    print(f"Suffix: {file_path.suffix}")
    print(f"Parent: {file_path.parent}")
    print(f"Exists: {file_path.exists()}")

    # Cleanup
    file_path.unlink()
    p.rmdir()
    print("Cleaned up")


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=== Writing Files ===")
    write_sample_file()
    append_to_file()

    print("\n=== Reading Files ===")
    read_entire_file()

    print("=== Line by Line ===")
    read_line_by_line()

    print("\n=== Binary Files ===")
    write_binary()
    read_binary()

    print("\n=== CSV Files ===")
    write_csv()
    print("Reading CSV:")
    read_csv()

    print("\n=== JSON Files ===")
    write_json()
    read_json()

    print("\n=== Pathlib ===")
    pathlib_demo()

    # Cleanup
    import os
    for f in ["sample.txt", "sample.bin", "sample.csv", "sample.json"]:
        if os.path.exists(f):
            os.remove(f)
    print("\nCleaned up temp files")


if __name__ == "__main__":
    main()
