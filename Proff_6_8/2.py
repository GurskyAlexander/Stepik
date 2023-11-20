from collections import Counter


def get_less_common(words: str) -> list[str]:
    result = Counter(words.lower().split()).most_common()[::-1]
    return [x[0] for x in result if x[1] == result[0][1]]


print(*sorted(get_less_common(input())), sep=', ')
