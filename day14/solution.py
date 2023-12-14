with open("input.txt") as input_file:
    field = [list(line) for line in input_file.read().strip().split("\n")]
    n, m = len(field), len(field[0])


def calc_total_load(field):
    return sum((field[i][j] == "O") * (n - i) for i in range(n) for j in range(m))


def tilt_north_south(field, dir):  # dir = 1 for north, -1 for south
    new_field = [["."] * m for _ in range(n)]
    for j in range(m):
        cubes = []
        rounds = []
        for i in range(n):
            if field[i][j] == "#":
                cubes.append(i)
            elif field[i][j] == "O":
                rounds.append(i)

        round_index = 0
        cube_index = 0
        cubes = [-1] + cubes + [n]  # add edges
        groups = {cube: 0 for cube in cubes}
        cubes, rounds = cubes[::dir], rounds[::dir]
        while round_index < len(rounds):
            cur_round = rounds[round_index]
            cur_cube, next_cube = cubes[cube_index], cubes[cube_index + 1]
            if dir * cur_cube < dir * cur_round < dir * next_cube:
                groups[cur_cube] += 1
                round_index += 1
            else:
                cube_index += 1

        for cube, rounds_count in groups.items():
            if 0 <= cube < n:
                new_field[cube][j] = "#"
            for k in range(rounds_count):
                new_field[cube + (k + 1) * dir][j] = "O"
    return new_field


def tilt_east_west(field, dir):  # dir = 1 for west, -1 for east
    new_field = [["."] * m for _ in range(n)]
    for i in range(n):
        cubes = []
        rounds = []
        for j in range(m):
            if field[i][j] == "#":
                cubes.append(j)
            elif field[i][j] == "O":
                rounds.append(j)

        round_index = 0
        cube_index = 0
        cubes = [-1] + cubes + [m]  # add edges
        groups = {cube: 0 for cube in cubes}
        cubes, rounds = cubes[::dir], rounds[::dir]
        while round_index < len(rounds):
            cur_round = rounds[round_index]
            cur_cube, next_cube = cubes[cube_index], cubes[cube_index + 1]
            if dir * cur_cube < dir * cur_round < dir * next_cube:
                groups[cur_cube] += 1
                round_index += 1
            else:
                cube_index += 1

        for cube, rounds_count in groups.items():
            if 0 <= cube < m:
                new_field[i][cube] = "#"
            for k in range(rounds_count):
                new_field[i][cube + (k + 1) * dir] = "O"
    return new_field


def do_cycle(field):
    field = tilt_north_south(field, dir=1)
    field = tilt_east_west(field, dir=1)
    field = tilt_north_south(field, dir=-1)
    field = tilt_east_west(field, dir=-1)
    return field


def calc_total_load_after_cycles(field, cycles):
    history = {}
    repeat, offset = None, None
    cur_field = field
    for k in range(cycles):
        cur_field = do_cycle(cur_field)
        cur_field = tuple(tuple(row) for row in cur_field)
        if cur_field in history:
            repeat, offset = k - history[cur_field], history[cur_field]
            break
        history[cur_field] = k

    target_offset = (cycles - offset) % repeat + offset - 1
    target_field = next(field for field, offset in history.items() if offset == target_offset)
    return calc_total_load(target_field)


print(calc_total_load(tilt_north_south(field, dir=1)))  # part 1
print(calc_total_load_after_cycles(field, cycles=1000000000))  # part 2
