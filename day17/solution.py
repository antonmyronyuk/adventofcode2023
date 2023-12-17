from heapq import heappop, heappush

with open("input.txt") as input_file:
    field = [[int(num) for num in line] for line in input_file.read().strip().split("\n")]
    n, m = len(field), len(field[0])
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def last(arr):
    return arr[-1] if arr else None


def equal_in_tail(path):
    count = 0
    for dir in reversed(path):
        if dir == last(path):
            count += 1
        else:
            break
    return count


def calc_min_loss_part1():
    queue = [(0, (0, 0), [])]
    visited = set()
    while queue:
        loss, (i, j), path = heappop(queue)
        cur_dir = last(path)
        visited_key = (i, j), cur_dir, equal_in_tail(path)
        if visited_key in visited:
            continue

        visited.add(visited_key)
        if (i, j) == (n - 1, m - 1):
            return loss

        for di, dj in dirs:
            if (-di, -dj) == cur_dir:
                continue

            ni, nj = i + di, j + dj
            if any([ni < 0, ni >= n, nj < 0, nj >= m]):
                continue

            if cur_dir == (di, dj) and equal_in_tail(path) == 3:
                continue

            heappush(queue, (loss + field[ni][nj], (ni, nj), path + [(di, dj)]))


def calc_min_loss_part2():
    queue = [(0, (0, 0), [])]
    visited = set()
    while queue:
        loss, (i, j), path = heappop(queue)
        cur_dir = last(path)
        visited_key = (i, j), cur_dir, equal_in_tail(path)
        if visited_key in visited:
            continue

        visited.add(visited_key)
        if (i, j) == (n - 1, m - 1):
            return loss

        for di, dj in dirs:
            if (-di, -dj) == cur_dir:
                continue

            ni, nj = i + di, j + dj
            if any([ni < 0, ni >= n, nj < 0, nj >= m]):
                continue

            if cur_dir == (di, dj) and equal_in_tail(path) == 10:
                continue

            if cur_dir and cur_dir != (di, dj) and equal_in_tail(path) < 4:
                continue

            heappush(queue, (loss + field[ni][nj], (ni, nj), path + [(di, dj)]))


print(calc_min_loss_part1())
print(calc_min_loss_part2())
