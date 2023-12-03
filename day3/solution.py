with open("input.txt") as input_file:
    lines = input_file.read().strip().split("\n")

# add border
n, m = len(lines) + 2, len(lines[0]) + 2
map = [["."] * m for _ in range(n)]
for i in range(1, n - 1):
    for j in range(1, m - 1):
        map[i][j] = lines[i - 1][j - 1]


def get_adjacent_chars_pos(i, j_start, j_end):
    chars = {(i, j_start - 1), (i, j_end)}
    chars.update((i - 1, j) for j in range(j_start - 1, j_end + 1))
    chars.update((i + 1, j) for j in range(j_start - 1, j_end + 1))
    return chars


def has_symbol(chars_pos):
    return any(map[i][j] for i, j in chars_pos if not (map[i][j].isdigit() or map[i][j] == "."))


def parse_numbers_with_adj_chars_pos():
    num = ""
    for i in range(n):
        for j in range(m):
            if map[i][j].isdigit():
                num += map[i][j]
            elif num:
                yield int(num), get_adjacent_chars_pos(i, j - len(num), j)
                num = ""


number_with_adj_chars_pos = list(parse_numbers_with_adj_chars_pos())

# part 1
print(sum(num for num, chars_pos in number_with_adj_chars_pos if has_symbol(chars_pos)))

# part 2
res = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == "*":
            adj_nums = [num for num, chars_pos in number_with_adj_chars_pos if (i, j) in chars_pos]
            if len(adj_nums) == 2:
                res += adj_nums[0] * adj_nums[1]

print(res)
