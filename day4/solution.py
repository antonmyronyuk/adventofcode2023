with open("input.txt") as input_file:
    lines = input_file.read().strip().split("\n")

cards = []
card_copies = {i: 1 for i in range(1, len(lines) + 1)}

for line in lines:
    winning_numbers_raw, numbers_raw = line.split(": ")[-1].split(" | ")
    winning_numbers = {int(num) for num in winning_numbers_raw.split()}
    numbers = {int(num) for num in numbers_raw.split()}
    cards.append((winning_numbers, numbers))

res_part1 = 0
res_part2 = 0
for i, (winning_numbers, numbers) in enumerate(cards, 1):
    num_matches = len(set(winning_numbers) & set(numbers))
    res_part1 += int(2 ** (num_matches - 1))
    res_part2 += card_copies[i]
    for j in range(i, i + num_matches):
        card_copies[j + 1] += card_copies[i]

print(res_part1)
print(res_part2)
