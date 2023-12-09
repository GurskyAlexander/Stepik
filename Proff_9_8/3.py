from functools import wraps
from typing import Callable


def trace(foo: Callable) -> Callable:
    """Декоратор выводит отладочную информацию о функции во время ее выполнения """

    @wraps(foo)
    def wrapper(*args, **kwargs):
        res = foo(*args, **kwargs)
        print(f'TRACE: вызов {foo.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {foo.__name__}(): {repr(res)}')
        return res

    return wrapper
