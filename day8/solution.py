from itertools import cycle
from math import lcm


with open("input.txt") as input_file:
    instructions, mapping_raw = input_file.read().strip().split("\n\n")
    mapping = {r[:3]: (r[7:10], r[12:15]) for r in mapping_raw.split("\n")}


def part1():
    node = "AAA"
    for step, instruction in enumerate(cycle(instructions), start=1):
        node = mapping[node][instruction == "R"]
        if node == "ZZZ":
            return step


def part2():
    nodes = [node for node in mapping if node.endswith("A")]
    n = len(nodes)
    targets = [0] * n
    for step, instruction in enumerate(cycle(instructions), start=1):
        for i in range(n):
            nodes[i] = mapping[nodes[i]][instruction == "R"]
            if nodes[i].endswith("Z") and not targets[i]:
                targets[i] = step

        if all(targets):
            return lcm(*targets)


print(part1())
print(part2())
