def get_sum(number: int) -> int:
    if number < 10:
        return number
    else:
        return number % 10 + get_sum(number // 10)


print(get_sum(int(input())))
