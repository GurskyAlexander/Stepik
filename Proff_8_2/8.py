def print_digits(number: int) -> str:
    if number > 0:
        print_digits(number // 10)
        print(number % 10)

print_digits(456)
