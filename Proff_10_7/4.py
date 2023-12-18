import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_headers = next(line_values)
    line_dicts = (dict(zip(file_headers, data)) for data in line_values)
    result = (dicts['raisedAmt'] for dicts in line_dicts if dicts['round'] == 'a')
    print(sum(map(int, result)))
