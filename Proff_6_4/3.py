# вывести построчно, отсортированный по дате и времени встречи, список друзей из файла meetings.csv (фамилию имя)
import csv
from collections import namedtuple
from datetime import datetime


Friend = namedtuple('Friend', ['surname', 'name', 'meeting_date', 'meeting_time'])
def get_datetime(seq: namedtuple) -> datetime:
    '''Функция возвращает дату и время встречи из именованного кортежа в формате datetime'''
    time = seq.meeting_date + ' ' + seq.meeting_time
    return datetime.strptime(time, '%d.%m.%Y %H:%M')


with open('meetings.csv', encoding='utf-8') as csv_file:
    friends = list(map(Friend._make, csv.reader(csv_file)))[1:]
    sorted_friends = sorted(friends, key=lambda x: get_datetime(x))
    for row in sorted_friends:
        print(row.surname, row.name)



