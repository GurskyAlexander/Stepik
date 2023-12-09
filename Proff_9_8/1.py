from functools import wraps


def square(foo):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        return foo(*args, **kwargs) ** 2

    return wrapper
