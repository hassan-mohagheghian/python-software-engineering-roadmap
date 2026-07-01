import sys

# --- read one one line with input: trim last \n ---
one_line = input("Enter you a line: ")
print("#####")
print(one_line)
print("#####")

# --- read one line with readline: include last \n ---
print("enter one line")
one_line = sys.stdin.readline()
print("#########")
print(one_line)
print("#########")
