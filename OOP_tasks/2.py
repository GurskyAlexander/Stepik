def check(seq: str) -> bool:
    a = {'(': 1, ')': -1}
    answer = 0
    for char in seq:
        answer += a[char]
        if answer < 0:
            return False
    return answer == 0


print(check(input()))
