from functools import wraps


def prefix(string: str, to_the_end: bool = False):
    def decorator(foo):
        @wraps(foo)
        def wrapper(*args, **kwargs):
            res = foo(*args, **kwargs)
            if to_the_end:
                return res + string
            else:
                return string + res

        return wrapper

    return decorator
