from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as file:
    content = Counter([char.lower() for char in file.read() if char.isalpha()])
    for key, value in sorted(content.items()):
        print(f'{key}: {value}')
