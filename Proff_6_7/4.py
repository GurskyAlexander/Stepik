from collections import Counter

food = Counter(input().split(','))
leight = max(map(len, food.keys()))

for key in sorted(food.keys()):
    price = sum(map(ord, key.replace(' ', '')))
    print(f'{key}{" " * (leight - len(key))}: {price} UC x {food[key]} = {price * food[key]} UC')
