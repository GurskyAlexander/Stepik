from datetime import date, timedelta


def years_days(year):
    start_date = date(year, 1, 1)
    while start_date.year == year:
        yield start_date
        start_date += timedelta(days=1)


dates = years_days(2077)

print(*dates)
