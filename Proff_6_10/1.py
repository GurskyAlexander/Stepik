from collections import ChainMap


def get_all_values(chainmap: ChainMap, key: str) -> list:
    return {d[key] for d in chainmap.maps if key in d}
