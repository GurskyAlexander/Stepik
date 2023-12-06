def print_operation_table(operation, rows, cols):
    result = [[operation(x, y) for y in range(1, cols + 1)] for x in range(1, rows + 1)]
    for row in result:
        print(*row)


print_operation_table(lambda a, b: a * b, 5, 5)