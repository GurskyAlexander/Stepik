def sandwich(func: function) -> function:
    def wrapper(*args, **kwargs):
        start = '---- Верхний ломтик хлеба ----'
        end = '---- Нижний ломтик хлеба ----'
        return start + '\n' + func(*args, **kwargs) + '\n' + end
    return wrapper()
