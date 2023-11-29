def foo(x=1, n=16):
    if x < 4:
        print(f'{str(x)*n: ^16}')
        foo(x+1, n-4)
    print(f'{str(x)*n: ^16}')

foo()
