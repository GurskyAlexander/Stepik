cash = {1: 1, 2: 1, 3: 1}


def tribonacci(num: int) -> int:
    result = cash.get(num)
    if result is None:
        result = tribonacci(num - 1) + tribonacci(num - 2) + tribonacci(num - 3)
        cash[num] = result
    return result


print(tribonacci(7))
