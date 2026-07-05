# Data Structures - List
# -----------------------------------------------------------------------------
# A list is an ordered, mutable collection.
#
# Use a list when:
#
# - Order matters.
# - Items may change over time.
# - You need to add, remove, or update items.
# - Duplicate values are allowed.
#
# -----------------------------------------------------------------------------
# Common list operations:
#
# - append: add an item to the end
# - insert: add an item at a specific index
# - remove: remove an item by value
# - pop: remove and return an item by index
# - indexing: access one item
# - slicing: access part of the list
# - iteration: process each item
# -----------------------------------------------------------------------------


def main():
    tasks = ["write code", "run tests", "review changes"]

    print("===== Original List =====")
    print(tasks)

    print("\n===== Add Items =====")
    tasks.append("commit changes")
    tasks.insert(1, "format code")
    print(tasks)

    print("\n===== Access Items =====")
    print(f"First task: {tasks[0]}")
    print(f"Last task: {tasks[-1]}")
    print(f"First two tasks: {tasks[:2]}")

    print("\n===== Update Item =====")
    tasks[0] = "write clean code"
    print(tasks)

    print("\n===== Remove Items =====")
    tasks.remove("review changes")
    completed_task = tasks.pop(0)
    print(f"Completed: {completed_task}")
    print(tasks)

    print("\n===== Iterate =====")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print("\n===== List Comprehension =====")
    uppercase_tasks = [task.upper() for task in tasks]
    print(uppercase_tasks)


if __name__ == "__main__":
    main()
