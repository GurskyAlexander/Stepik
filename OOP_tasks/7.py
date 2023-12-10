def quantify(iterable, predicate):
    if predicate is None:
        predicate = bool
    return sum(map(predicate, iterable))
