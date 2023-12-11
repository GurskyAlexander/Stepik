from functools import wraps


def returns(datatype):
    def decorator(foo):
        @wraps(foo)
        def wrapper(*args, **kwargs):
            res = foo(*args, **kwargs)
            if not isinstance(res, datatype):
                raise TypeError
            return res

        return wrapper

    return decorator
