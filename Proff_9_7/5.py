def exception_decorator(foo):
    def wrapper(*args, **kwargs):
        try:
            res = foo(*args, **kwargs)
            return res, 'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'

    return wrapper


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1


print(f(7))
