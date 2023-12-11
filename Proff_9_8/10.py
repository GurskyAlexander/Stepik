from functools import wraps


def add_attrs(**kwargs_):
    def decorator(foo):
        for key, value in kwargs_.items():
            foo.__dict__[key] = value
        @wraps(foo)
        def wrapper(*args, **kwargs):
            res = foo(*args, **kwargs)
            return res

        return wrapper

    return decorator
