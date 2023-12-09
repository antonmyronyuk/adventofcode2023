def predict_next_value(nums: list[int]) -> int:
    last_diffs = []
    diffs = nums
    while any(diffs):
        diffs = [b - a for a, b in zip(diffs, diffs[1:])]
        last_diffs.append(diffs[-1])

    return nums[-1] + sum(last_diffs)


def predict_prev_value(nums: list[int]) -> int:
    first_diffs = []
    diffs = nums
    sign = 1
    while any(diffs):
        diffs = [b - a for a, b in zip(diffs, diffs[1:])]
        first_diffs.append(sign * diffs[0])
        sign *= -1

    return nums[0] - sum(first_diffs)


with open("input.txt") as input_file:
    lines = [list(map(int, line.split())) for line in input_file.read().strip().split("\n")]


print(sum(predict_next_value(line) for line in lines))  # part 1
print(sum(predict_prev_value(line) for line in lines))  # part 2
