def number_of_frogs(year: int, n=77) -> int:
    if year == 1:
        return n
    else:
        return 3 * (number_of_frogs(year - 1) - 30)

print(number_of_frogs(2))