from functools import wraps


def make_html(tag: str):
    def decorator(foo):
        @wraps(foo)
        def wrapper(*args, **kwargs):
            start = f'<{tag}>'
            end = f'</{tag}>'
            res = foo(*args, **kwargs)
            return start + res + end

        return wrapper

    return decorator
