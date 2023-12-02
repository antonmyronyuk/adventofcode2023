limits_by_color = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("input.txt") as input_file:
    games = input_file.read().strip().split("\n")


def is_possible_game(game_data):
    return all(
        all(counts[color] <= limits_by_color[color] for color in counts)
        for counts in game_data
    )


def get_min_possible_counts(game_data):
    return {
        color: max(counts.get(color, 0) for counts in game_data)
        for color in limits_by_color
    }


res_part1 = 0
res_part2 = 0

for game_id, game in enumerate(games, 1):
    combinations = [comb.strip().split(", ") for comb in game.split(":")[1].strip().split(";")]
    game_data = [
        {color: int(count) for count, color in map(str.split, combination)}
        for combination in combinations
    ]
    if is_possible_game(game_data):
        res_part1 += game_id

    min_counts = get_min_possible_counts(game_data)
    res_part2 += min_counts["red"] * min_counts["green"] * min_counts["blue"]

print(res_part1)
print(res_part2)
