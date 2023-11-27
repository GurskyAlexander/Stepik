def get_id(names: list, name: str) -> int:
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    return len(names) + 1