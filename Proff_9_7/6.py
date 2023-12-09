def takes_positive(foo):
    def wrapper(*args, **kwargs):
        if not all(map(lambda x: isinstance(x, int), (*args, *kwargs.values()))):
            raise TypeError
        if not all(map(lambda x: x > 0, (*args, *kwargs.values()))):
            raise ValueError



        res = foo(*args, **kwargs)
        return res
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(*range(100, -1, -1)))
except Exception as err:
    print(type(err))