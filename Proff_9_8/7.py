from functools import wraps


def strip_range(start, end, char='.'):
    def decorator(foo):
        @wraps(foo)
        def wrapper(*args, **kwargs):
            res = list(foo(*args, **kwargs))
            for i in range(start, min(end, len(res))):
                res[i] = char
            return ''.join(res)

        return wrapper

    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())
