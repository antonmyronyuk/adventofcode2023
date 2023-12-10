from collections import deque

connections = {
    "|": {"up": ("|", "7", "F"), "down": ("|", "L", "J"), "left": (), "right": ()},
    "-": {"up": (), "down": (), "left": ("-", "L", "F"), "right": ("-", "J", "7")},
    "L": {"up": ("|", "7", "F"), "down": (), "left": (), "right": ("-", "J", "7")},
    "J": {"up": ("|", "7", "F"), "down": (), "left": ("-", "L", "F"), "right": ()},
    "7": {"up": (), "down": ("|", "L", "J"), "left": ("-", "L", "F"), "right": ()},
    "F": {"up": (), "down": ("|", "L", "J"), "left": (), "right": ("-", "J", "7")},
}
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

with open("input.txt") as input_file:
    maze = [list(line) for line in input_file.read().strip().split("\n")]
    n, m = len(maze), len(maze[0])
    visited_map = [[-1] * m for _ in range(n)]

start_i, start_j = next((i, j) for i in range(n) for j in range(m) if maze[i][j] == "S")
visited_map[start_i][start_j] = 0

# get start tile
for tile, connection in connections.items():
    if all(
        not connection[direction] or maze[start_i + di][start_j + dj] in connection[direction]
        for direction, (di, dj) in directions.items()
    ):
        maze[start_i][start_j] = tile


queue = deque([(start_i, start_j)])
while queue:
    i, j = queue.popleft()
    distance = visited_map[i][j]
    for direction, (di, dj) in directions.items():
        ni, nj = i + di, j + dj
        if (
            0 <= ni < n
            and 0 <= nj < m
            and maze[ni][nj] in connections[maze[i][j]][direction]
            and visited_map[ni][nj] == -1
        ):
            visited_map[ni][nj] = distance + 1
            queue.append((ni, nj))

print(max(max(row) for row in visited_map))  # part 1

# part 2
bn, bm = 3 * n, 3 * m
big_maze = [["."] * bm for _ in range(bn)]
seen_map = [[False] * bm for _ in range(bn)]
for i in range(n):
    for j in range(m):
        # skip items that are not part of main loop, use visited_map from part 1
        if visited_map[i][j] == -1:
            continue

        bi, bj = 3 * i, 3 * j
        match maze[i][j]:
            case "|":
                big_maze[bi][bj + 1] = "|"
                big_maze[bi + 1][bj + 1] = "|"
                big_maze[bi + 2][bj + 1] = "|"
            case "-":
                big_maze[bi + 1][bj] = "-"
                big_maze[bi + 1][bj + 1] = "-"
                big_maze[bi + 1][bj + 2] = "-"
            case "L":
                big_maze[bi][bj + 1] = "|"
                big_maze[bi + 1][bj + 1] = "L"
                big_maze[bi + 1][bj + 2] = "-"
            case "J":
                big_maze[bi][bj + 1] = "|"
                big_maze[bi + 1][bj + 1] = "J"
                big_maze[bi + 1][bj] = "-"
            case "7":
                big_maze[bi + 1][bj] = "-"
                big_maze[bi + 1][bj + 1] = "7"
                big_maze[bi + 2][bj + 1] = "|"
            case "F":
                big_maze[bi + 1][bj + 2] = "-"
                big_maze[bi + 1][bj + 1] = "F"
                big_maze[bi + 2][bj + 1] = "|"

# start move from any border
queue = deque()
for i in range(bn):
    for j in range(bm):
        if (i in (0, bn - 1) or j in (0, bn - 1)) and big_maze[i][j] == ".":
            queue.append((i, j))

while queue:
    i, j = queue.popleft()
    if seen_map[i][j]:
        continue

    seen_map[i][j] = True
    for di, dj in directions.values():
        ni, nj = i + di, j + dj
        if (
            0 <= ni < bn
            and 0 <= nj < bm
            and big_maze[ni][nj] == "."
            and not seen_map[ni][nj]
        ):
            queue.append((ni, nj))

res = 0
for i in range(n):
    for j in range(m):
        bi, bj = 3 * i, 3 * j
        res += all(not seen_map[bi + di][bj + dj] for di in range(3) for dj in range(3))
print(res)
