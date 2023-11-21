from collections import Counter


def scrabble(symbols: str, word: str) -> bool:
    return Counter(word.lower()) <= Counter(symbols.lower())


a, b = 'bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'

print(scrabble(a, b))
