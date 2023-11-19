from collections import Counter

for key, value in sorted(Counter(input().split(',')).items()):
    print(f'{key}: {value}')