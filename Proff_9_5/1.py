def sort_priority(values: list, group: (set, list, tuple)) -> None:
    def comparator(x):
        return not x in group, x

    values.sort(key=lambda x: comparator(x))


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)
