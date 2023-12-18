from collections import deque

with open("input.txt") as input_file:
    moves = input_file.read().strip().split("\n")

dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
n, m = 1000, 1000
field = [["."] * m for _ in range(m)]

# draw border
i, j = 500, 500
field[i][j] = "#"
for move in moves:
    dir, length, color = move.split(" ")
    di, dj = dirs[dir]
    for _ in range(int(length)):
        i, j = i + di, j + dj
        field[i][j] = "#"


def save_img(filename):
    from PIL import Image
    img = Image.new("RGB", (m, n))
    for i in range(n):
        for j in range(m):
            color = (0, 0, 0) if field[i][j] == "#" else (160, 160, 60)
            img.putpixel((j, i), color)
    img.save(filename)


def calc_size(start):
    queue = deque([start])
    while queue:
        i, j = queue.popleft()
        if field[i][j] == "#":
            continue

        field[i][j] = "#"
        for di, dj in dirs.values():
            ni, nj = i + di, j + dj
            if all([ni >= 0, ni < n, nj >= 0, nj < n]) and field[ni][nj] != "#":
                queue.append((ni, nj))

    return sum(field[i][j] == "#" for i in range(n) for j in range(m))


# part 1
save_img("before.png")
print(calc_size((501, 501)))  # start point was chosen visually on image
save_img("after.png")
