# exit with specific termination

print("Enter you lines, exit with a blank line")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

result = "\n".join(lines)
print("#####")
print(result)
print("#####")
