import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number):
    try:
        if isinstance(number, int):
            if number in range(1, 8):
                return calendar.day_name[number - 1]
            else:
                raise ValueError('Аргумент не принадлежит требуемому диапазону')
        else:
            raise TypeError('Аргумент не является целым числом')
    except Exception:
        raise
