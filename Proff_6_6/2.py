from collections import OrderedDict


data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

new_data = OrderedDict()

for _ in range(len(data) // 2):
    for rule in (False, True):
        key, value = data.popitem(last=rule)
        new_data[key] = value

print(new_data)
