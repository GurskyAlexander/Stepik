from functools import wraps


def ignore_exception(*exceptions):
    def decorator(foo):
        @wraps(foo)
        def wrapper(*args, **kwargs):
            try:
                res = foo(*args, **kwargs)
            except exceptions as err:
                print(f'Исключение {err} обработано')
            except Exception as er:
                raise er
            else:
                return res

        return wrapper

    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)