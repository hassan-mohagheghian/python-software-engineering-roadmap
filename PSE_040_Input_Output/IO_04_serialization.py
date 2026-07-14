# Input/Output - Serialization
# -----------------------------------------------------------------------------
# Serialization converts Python objects to bytes/strings for storage
# or transmission. Deserialization reverses the process.
#
# Key concepts:
# 1. JSON — human-readable, cross-language
# 2. pickle — Python-specific, can serialize most objects
# 3. csv — tabular data
# 4. Custom serialization
# -----------------------------------------------------------------------------


import csv
import json
import os
import pickle
from io import StringIO

# =============================================================================
# JSON
# =============================================================================


# Serialize
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}
json_str = json.dumps(data, indent=2)
print(f"JSON:\n{json_str}")

# Deserialize
parsed = json.loads(json_str)
print(f"Parsed: {parsed}")

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json") as f:
    loaded = json.load(f)
print(f"Loaded: {loaded}")


# =============================================================================
# CSV
# =============================================================================


# Write CSV
output = StringIO()
writer = csv.writer(output)
writer.writerow(["Name", "Age", "City"])
writer.writerow(["Alice", 30, "NYC"])
writer.writerow(["Bob", 25, "LA"])
csv_content = output.getvalue()
print(f"\nCSV:\n{csv_content}")

# Read CSV
reader = csv.DictReader(StringIO(csv_content))
for row in reader:
    print(f"  {row['Name']}, {row['Age']}, {row['City']}")


# =============================================================================
# Pickle (Python-specific)
# =============================================================================


# Serialize
data = {"users": ["Alice", "Bob"], "count": 2}
pickled = pickle.dumps(data)

# Deserialize
unpickled = pickle.loads(pickled)
print(f"\nPickle: {unpickled}")


# Cleanup


os.remove("data.json")


def main():
    print("=== Serialization ===")
    data = {"key": "value", "numbers": [1, 2, 3]}
    json_str = json.dumps(data)
    print(f"JSON: {json_str}")
    print(f"Restored: {json.loads(json_str)}")


if __name__ == "__main__":
    main()
