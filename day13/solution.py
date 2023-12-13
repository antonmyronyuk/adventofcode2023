def get_horizontal_cross(pattern, diff=0):
    for cross in range(1, len(pattern)):
        size = min(cross, len(pattern) - cross)
        if sum(
            pattern[cross - i - 1][j] == pattern[cross + i][j]
            for i in range(size) for j in range(len(pattern[0]))
        ) == size * len(pattern[0]) - diff:
            return cross
    return 0


def get_vertical_cross(pattern, diff=0):
    for cross in range(1, len(pattern[0])):
        size = min(cross, len(pattern[0]) - cross)
        if sum(
            pattern[i][cross - j - 1] == pattern[i][cross + j]
            for i in range(len(pattern)) for j in range(size)
        ) == size * len(pattern) - diff:
            return cross
    return 0


def solve(patterns, diff):
    return sum(
        100 * get_horizontal_cross(pattern, diff) + get_vertical_cross(pattern, diff)
        for pattern in patterns
    )


with open("input.txt") as input_file:
    patterns = [pattern.split("\n") for pattern in input_file.read().strip().split("\n\n")]

print(solve(patterns, diff=0))  # part 1
print(solve(patterns, diff=1))  # part 2
