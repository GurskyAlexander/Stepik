from functools import wraps
import json


def jsonify(foo):
    '''Декоратор, переводит то что возвращает функция в json формат'''

    @wraps(foo)
    def wrapper(*args, **kwargs):
        res = foo(*args, **kwargs)
        return json.dumps(res)

    return wrapper


@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}


print(make_user(4, False, None))
