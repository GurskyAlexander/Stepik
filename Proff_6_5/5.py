from collections import defaultdict


def flip_dict(dict_of_lists: dict) -> dict:
    flip_result = defaultdict(list)
    for key, value in dict_of_lists.items():
        for item in value:
            flip_result[item].append(key)
    return flip_result
