def get_fast_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    elif n % 2:
        return a * get_fast_pow(a, n - 1)
    return get_fast_pow(a * a, n // 2)


print(get_fast_pow(2, 10))