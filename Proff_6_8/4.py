from collections import Counter

words = input()

result = Counter(map(len, words.lower().split()))

for key in sorted(result, key=lambda x: result[x]):
    print(f'Слов длины {key}: {result[key]}')
