import sys

log_entries = sys.stdin.read().strip().split("\n")
for entry in log_entries:
    if "ERROR" in entry:
        print(f"Found error: {entry}")
    