import calendar


def get_month_name(date: str) -> str:
    try:
        date = int(date)
        1 / (abs(date) + date)
        return calendar.month_name[date]
    except (TypeError, ValueError):
        return 'Введено некорректное значение'
    except:
        return 'Введено число из недопустимого диапазона'


print(get_month_name(input()))
