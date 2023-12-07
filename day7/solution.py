from collections import Counter

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_rank = {card: rank for rank, card in enumerate(cards, 2)}
card_rank_joker = {**card_rank, "J": 1}


def get_rank(comb):
    type_rank = [num for card, num in Counter(comb).most_common(2)]
    strongest_card_rank = [card_rank[card] for card in comb]
    return type_rank + strongest_card_rank


def get_rank_joker(comb):
    max_type_rank = [num for card, num in Counter(comb).most_common(2)]
    for card in cards:
        type_rank = [num for card, num in Counter(comb.replace("J", card)).most_common(2)]
        max_type_rank = max(type_rank, max_type_rank)

    strongest_card_rank = [card_rank_joker[card] for card in comb]
    return max_type_rank + strongest_card_rank


with open("input.txt") as input_file:
    pairs = [line.split() for line in input_file.read().strip().split("\n")]

sorted_part1 = sorted(pairs, key=lambda pair: get_rank(pair[0]))
print(sum(int(bid) * i for i, (_, bid) in enumerate(sorted_part1, 1)))

sorted_part2 = sorted(pairs, key=lambda pair: get_rank_joker(pair[0]))
print(sum(int(bid) * i for i, (_, bid) in enumerate(sorted_part2, 1)))
