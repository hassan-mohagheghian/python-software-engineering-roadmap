n = int(input("How many liens? "))
lines = [input(f"Line {i+1}: ") for i in range(n)]

print("#####")
print("\n".join(lines))
print("#####")
