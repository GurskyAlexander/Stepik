from functools import wraps


def takes(*args_):
    def decorator(foo):
        @wraps(foo)
        def wrapper(*args, **kwargs):
            for arg in (*args, *kwargs.values()):
                if type(arg) not in args_:
                    raise TypeError
            res = foo(*args, **kwargs)
            return res

        return wrapper

    return decorator

@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))

@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))
