from functools import wraps


def repeat(times: int):
    def decorator(foo):
        @wraps(foo)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                res = foo(*args, **kwargs)
            return res

        return wrapper

    return decorator
