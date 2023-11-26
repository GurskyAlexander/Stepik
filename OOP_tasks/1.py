n = int(input())

matrix = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = min(i + 1, j + 1, n - i, n - j)

for row in matrix:
    print(*row)
