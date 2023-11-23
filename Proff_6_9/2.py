from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

burger = ChainMap(bread, meat, sauce, vegetables, toppings)
ingrs = Counter(input().split(','))
total = sum(map(lambda x: burger[x] * ingrs[x], ingrs))
max_l = max(map(len, ingrs))
check = []

for key, value in sorted(ingrs.items()):
    check.append(f'{key.ljust(max_l)} x {value}')

check.append(f'ИТОГ: {total}р')

print(*check[:-1], sep='\n')
print('-' * max(map(len, check)))
print(check[-1])
