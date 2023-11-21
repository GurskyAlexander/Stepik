from collections import Counter
import csv, json

files = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']
counter = Counter()

with open('prices.json', encoding='utf-8') as json_file:
    prices = json.load(json_file)

for file in files:
    with open(file, encoding='utf-8') as csv_file:
        data = csv.reader(csv_file)
        next(data)
        for key, *count in data:
            counter += {key: sum(map(int, count)) * prices[key]}

print(counter.total())
