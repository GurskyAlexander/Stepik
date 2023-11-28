def is_good_password(string: str) -> bool:
    if len(string) < 9:
        return False
    a = any(char.isdigit for char in string)
    b = any(char.isalpha() and char.isupper() for char in string)
    c = any(char.isalpha() and char.islower() for char in string)
    return all([a, b, c])
