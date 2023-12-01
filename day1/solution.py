digits_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("input.txt") as input_file:
    lines = [line for line in input_file.read().split("\n") if line]


def get_first(line: str):
    for end in range(len(line)):
        if line[end].isdigit():
            return line[end]

        for digit in digits_map:
            if line[:end + 1].endswith(digit):
                return digits_map[digit]


def get_last(line: str):
    for start in range(len(line) - 1, -1, -1):
        if line[start].isdigit():
            return line[start]

        for digit in digits_map:
            if line[start:].startswith(digit):
                return digits_map[digit]


res_part1 = 0
for line in lines:
    filtered = [char for char in line if char.isdigit()]
    first, last = filtered[0], filtered[-1]
    res_part1 += int(first + last)

print(res_part1)


res_part2 = 0
for line in lines:
    first, last = get_first(line), get_last(line)
    res_part2 += int(first + last)

print(res_part2)
