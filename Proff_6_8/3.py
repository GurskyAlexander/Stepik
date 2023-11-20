from collections import Counter


def get_most_common(words: str) -> str:
    result = Counter(words.lower().split()).most_common()
    return max([x[0] for x in result if x[1] == result[0][1]])


print(get_most_common(input()))
