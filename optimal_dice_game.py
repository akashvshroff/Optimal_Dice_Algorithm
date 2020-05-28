from collections import defaultdict
from itertools import combinations


def count_wins(dice_ref, dice1, dice2):  # returns dice1 or dice2 depending on which one is better
    dice1_wins, dice2_wins = 0, 0
    plays = 0
    for i in dice_ref[dice1]:
        for j in dice_ref[dice2]:
            plays += 1
            if i > j:
                dice1_wins += 1
            elif j > i:
                dice2_wins += 1

    if dice1_wins > dice2_wins:
        return dice1, dice2, dice1_wins/plays
    elif dice2_wins > dice1_wins:
        return dice2, dice1, dice2_wins/plays


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    strategy = dict()
    strategy['choose_first'] = False
    ultimate_dice = None
    can_lose = defaultdict(list)
    dice_ref = {}
    for i, dice in enumerate(dices):
        dice_ref[i] = dice
    for d1, d2 in combinations(range(len(dices)), 2):
        stats = count_wins(dice_ref, d1, d2)
        if not stats:
            continue
        else:
            winner, loser, perc = stats
        can_lose[loser].append([winner, perc])
    if any(id not in can_lose for id in dice_ref):
        ultimate_dice = id
    if ultimate_dice:
        strategy['choose_first'] = True
        strategy['first_dice'] = ultimate_dice
    else:
        for id, stats in can_lose.items():
            can_lose[id].sort(key=lambda x: x[1], reverse=True)
            strategy[id] = can_lose[id][0][0]
    return strategy


print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))
