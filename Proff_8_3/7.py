def recursive_sum(a: int, b: int) -> int:
    if a == 0:
        return b
    else:
        return recursive_sum(a - 1, b + 1)


print(recursive_sum(10, 25))
