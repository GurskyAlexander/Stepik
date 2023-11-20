from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['min_values'] = lambda: [(key, value) for key, value in data.items() if value == min(data.values())]
data.__dict__['max_values'] = lambda: [(key, value) for key, value in data.items() if value == max(data.values())]

print(data.min_values())
print(data.max_values())
