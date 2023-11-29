def foo(n, count=0):
    if n // 10 == 0:
        return 1
    else:
        return 1 + foo(n // 10)

print(foo(34067))