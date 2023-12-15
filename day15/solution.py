def hash_string(string):
    res = 0
    for char in string:
        res += ord(char)
        res *= 17
        res %= 256
    return res


with open("input.txt") as input_file:
    commands = input_file.read().strip().split(",")


boxes = [{} for _ in range(256)]
for command in commands:
    if "=" in command:
        label, length = command.split("=")
        boxes[hash_string(label)][label] = int(length)  # python dict keeps insertion order
    else:
        label = command.removesuffix("-")
        boxes[hash_string(label)].pop(label, 0)


print(sum(hash_string(command) for command in commands))  # part 1
print(sum(i * j * length for i, box in enumerate(boxes, 1) for j, length in enumerate(box.values(), 1)))  # part 2
