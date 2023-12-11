with open("input.txt") as input_file:
    map = [list(line) for line in input_file.read().strip().split("\n")]

n, m = len(map), len(map[0])
galaxies = [(i, j) for i in range(n) for j in range(m) if map[i][j] == "#"]
empty_rows = [i for i in range(n) if all(item == "." for item in map[i])]
empty_cols = [j for j in range(m) if all(row[j] == "." for row in map)]


def calc_distance(mul):
    res = 0
    for k, (start_i, start_j) in enumerate(galaxies):
        for (end_i, end_j) in galaxies[k + 1:]:
            min_i, max_i = (start_i, end_i) if start_i < end_i else (end_i, start_i)
            min_j, max_j = (start_j, end_j) if start_j < end_j else (end_j, start_j)
            num_empty_rows = len([i for i in empty_rows if min_i < i < max_i])
            num_empty_cols = len([j for j in empty_cols if min_j < j < max_j])
            res += max_i - min_i + max_j - min_j + (mul - 1) * (num_empty_rows + num_empty_cols)
    return res


print(calc_distance(mul=2))  # part 1
print(calc_distance(mul=1000000))  # part 2
