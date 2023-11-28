class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str) -> bool:
    if len(string) < 9:
        raise LengthError('LengthError')
    b = any(char.isalpha() and char.isupper() for char in string)
    c = any(char.isalpha() and char.islower() for char in string)
    if not all([b, c]):
        raise LetterError('LetterError')
    if not any(char.isdigit() for char in string):
        raise DigitError('DigitError')
    return True


while True:
    try:
        if is_good_password(input()):
            print('Success!')
            break
    except PasswordError as err:
        print(err)
