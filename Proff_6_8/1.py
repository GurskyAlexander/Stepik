from collections import Counter


def get_most_common(words: str) -> str:
    return Counter(words.lower().split()).most_common()[0][0]


print(get_most_common(input()))
