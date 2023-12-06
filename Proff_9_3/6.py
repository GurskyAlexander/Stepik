import string


def verification(login, password, success, failure):
    password = set(password)
    check = {1: 0, 2: 0, 3: 0, 4: 0}
    d = {1: 'в пароле нет ни одной буквы',
         2: 'в пароле нет ни одной заглавной буквы',
         3: 'в пароле нет ни одной строчной буквы',
         4: 'в пароле нет ни одной цифры'}
    for char in password:
        if char in string.ascii_letters:
            check[1] = check.get(1, 0) + 1
            if char.isupper():
                check[2] = check.get(2, 0) + 1
            else:
                check[3] = check.get(3, 0) + 1
        elif char.isdigit():
            check[4] = check.get(4, 0) + 1
    if all(check.values()):
        return success(login)
    else:
        for key, value in check.items():
            if not value:
                return failure(login, d[key])


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпароль123', success, failure)