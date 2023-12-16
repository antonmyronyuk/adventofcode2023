from collections import defaultdict, deque

with open("input.txt") as input_file:
    field = input_file.read().strip().split("\n")
    n, m = len(field), len(field[0])

up, down, right, left = (-1, 0), (1, 0), (0, 1), (0, -1)
move_map = {
    "\\": {up: [left], left: [up], down: [right], right: [down]},
    "/": {up: [right], right: [up], down: [left], left: [down]},
    ".": {up: [up], down: [down], right: [right], left: [left]},
    "-": {up: [left, right], down: [left, right], right: [right], left: [left]},
    "|": {up: [up], down: [down], right: [up, down], left: [up, down]},
}


def calc_energized(start, dir):
    visited = defaultdict(list)
    queue = deque([(start, dir)])
    while queue:
        (i, j), dir = queue.popleft()
        if any([i < 0, i >= n, j < 0, j >= m]):
            continue

        if (i, j) in visited and dir in visited[i, j]:
            continue

        visited[i, j].append(dir)
        for next_dir in move_map[field[i][j]][dir]:
            queue.append(((i + next_dir[0], j + next_dir[1]), next_dir))

    return len(visited)


print(calc_energized((0, 0), right))  # part 1

start_pos = []
for i in range(n):
    start_pos.append(((i, 0), right))
    start_pos.append(((i, m - 1), left))
for j in range(m):
    start_pos.append(((0, j), down))
    start_pos.append(((n - 1, j), up))

print(max(calc_energized(start, dir) for start, dir in start_pos))  # part 2
