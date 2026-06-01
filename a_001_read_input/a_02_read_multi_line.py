import sys

# --- read multi line with read ---
print("please enter a multi-line. exit with EOF")
multi_line = sys.stdin.read()
print(multi_line)


# --- read multi line with sys.stdin.readlines ---
# return a list each one with trailing \n
print("please enter a multi-line. exit with EOF")
multi_line = sys.stdin.readlines()
print(multi_line)
