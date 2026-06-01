import file1

print("file1.counter before and after file1.increment")
print(file1.counter)
file1.increment()
print(file1.counter)


local_counter = 0


def increment():
    global local_counter
    local_counter += 1
    file1.counter += 1


increment()


print(f"local_counter: {local_counter}")
print(f"file1.counter after new increment: {file1.counter}")
