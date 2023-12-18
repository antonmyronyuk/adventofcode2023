import numpy as np

dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
with open("input.txt") as input_file:
    moves = input_file.read().strip().split("\n")


def get_coords_part1():
    i, j = 0, 0
    coords = [(i, j)]
    for move in moves:
        dir, length_raw, color = move.split(" ")
        length = int(length_raw)
        di, dj = dirs[dir]
        i, j = i + di * length, j + dj * length
        coords.append((i, j))
    return coords


def get_coords_part2():
    i, j = 0, 0
    coords = [(i, j)]
    for move in moves:
        color = move.split(" ")[-1].removeprefix("(#").removesuffix(")")
        length, dir_id = int(color[:5], 16), int(color[5]),
        dir = "RDLU"[dir_id]
        di, dj = dirs[dir]
        i, j = i + di * int(length), j + dj * int(length)
        coords.append((i, j))
    return coords


def calc_polygon_perimeter(coords):
    return sum(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in zip(coords, coords[1:]))


def calc_polygon_area(coords):
    # https://en.wikipedia.org/wiki/Shoelace_formula
    x = np.array([point[0] for point in coords])
    y = np.array([point[1] for point in coords])
    return abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))) // 2


def calc_res(coords):
    return calc_polygon_area(coords) + calc_polygon_perimeter(coords) // 2 + 1


print(calc_res(get_coords_part1()))
print(calc_res(get_coords_part2()))
