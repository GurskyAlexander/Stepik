from collections import defaultdict


def wins(pairs: list) -> dict:
    win_dict = defaultdict(set)
    for winer, looser in pairs:
        win_dict[winer].add(looser)
    return win_dict