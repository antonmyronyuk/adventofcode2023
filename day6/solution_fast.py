import math
from functools import reduce
from operator import mul


def calc_winning_races(t, d):
    discr_root = math.sqrt(t * t - 4 * d)
    start, end = math.ceil((t - discr_root) / 2), math.floor((t + discr_root) / 2)
    return end - start + 1


with open("input.txt") as input_file:
    lines = input_file.read().strip().split("\n")
    times, distances = [list(map(int, line.split(":")[1].split())) for line in lines]

# part 1
print(reduce(mul, (calc_winning_races(t, d) for t, d in zip(times, distances))))

# part 2
time, distance = int("".join(map(str, times))), int("".join(map(str, distances)))
print(calc_winning_races(time, distance))
