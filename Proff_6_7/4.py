from collections import Counter

food = Counter(input().split(','))
leght = max(map(len, food.keys()))

for key in sorted(food.keys()):
    price = sum(map(ord, key.replace(' ', '')))
    print(f'{key}{" " * (leght - len(key))}: {price} UC x {food[key]} = {price * food[key]} UC')
