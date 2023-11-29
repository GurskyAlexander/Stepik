def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 7):
    print(fib(i))

# ===================================

cash = {1: 1, 2: 2}


def fibb(n):
    result = cash.get(n)
    if result is None:
        result = fibb(n - 1) + fibb(n - 2)
        cash[n] = result
    return result


print(fibb(10))


#======================================================

fuct = lambda n: 1 if n == 0 else n * fuct(n-1)
print(*map(fuct, range(1, 11)))
