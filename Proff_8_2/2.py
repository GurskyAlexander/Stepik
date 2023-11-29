def foo():
    def rec(n):
        if n <= 100:
            print(n)
            rec(n + 1)
    rec(1)

foo()