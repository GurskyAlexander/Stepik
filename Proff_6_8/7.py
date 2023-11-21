import csv
from collections import Counter

with open('name_log.csv', encoding='utf-8') as csv_file:
    writer = csv.DictReader(csv_file)
    emails = Counter([x['email'] for x in writer])
    for key, value in sorted(emails.items()):
        print(f'{key}: {value}')
