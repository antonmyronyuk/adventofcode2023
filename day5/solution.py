from functools import reduce
from operator import add


def to_ints(row):
    return list(map(int, row.split()))


def convert(num, rule):
    return next((num + dst - src for dst, src, length in rule if src <= num < src + length), num)


def convert_range(num_range, rule):
    res_range = []
    for dst, src, length in rule:
        next_range = []
        while num_range:
            num_start, num_end = num_range.pop()
            src_start, src_end = src, src + length
            left_start, left_end = num_start, min(num_end, src_start)
            inner_start, inner_end = max(num_start, src_start), min(src_end, num_end)
            right_start, right_end = max(src_end, num_start), num_end
            if left_start < left_end:
                next_range.append((left_start, left_end))
            if right_start < right_end:
                next_range.append((right_start, right_end))
            if inner_start < inner_end:
                res_range.append((inner_start + dst - src, inner_end + dst - src))
        num_range = next_range
    return res_range + num_range


with open("input.txt") as input_file:
    blocks = input_file.read().strip().split("\n\n")
    seeds = to_ints(blocks[0].split(": ")[1])
    rules = [
        [to_ints(row) for row in rule_block.split("\n")[1:]]
        for rule_block in blocks[1:]
    ]

# part 1
print(min(reduce(convert, rules, seed) for seed in seeds))

# part 2
ranges_nested = [
    reduce(convert_range, rules, [(start, start + length)])
    for start, length in zip(seeds[::2], seeds[1::2])
]
min_range = min(reduce(add, ranges_nested))
print(min_range[0])
