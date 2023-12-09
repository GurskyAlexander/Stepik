from functools import wraps


def returns_string(foo):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        res = foo(*args, **kwargs)
        if not isinstance(res, str):
            raise TypeError
        return res

    return wrapper
