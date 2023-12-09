def reverse_args(foo):
    def wrapper(*args, **kwargs):
        a = foo(*args[::-1], **kwargs)
        return a
    return wrapper


@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))
