def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {i: matrix[i-1] for i in range(1, len(matrix) + 1)}


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))
