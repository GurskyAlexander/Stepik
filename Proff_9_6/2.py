def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step > 0:
        for _ in range(step):
            numbers.insert(0, numbers.pop())
    else:
        for _ in range(abs(step)):
            numbers.append(numbers.pop(0))


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -3)

print(numbers)
