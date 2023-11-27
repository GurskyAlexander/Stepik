import json

file_name = input()

try:
    with open(file_name, encoding='utf-8') as json_file:
        print(json.load(json_file))
except FileNotFoundError:
    print('Файл не найден')
except ValueError:
    print('Ошибка при десериализации')
