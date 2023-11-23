from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value) -> None:
    if key in chainmap.keys():
        for item in chainmap.maps:
            if key in item:
                item[key] = value
    else:
        chainmap[key] = value