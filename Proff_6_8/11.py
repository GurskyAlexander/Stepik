from collections import Counter


books = Counter(map(int, input().split()))
num = int(input())
total = 0
for _ in range(num):
    grade, price = map(int, input().split())
    if grade in books:
        books -= {grade: 1}
        total += price

print(total)
