def remainder(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a % b
