def is_prime(number: int) -> bool:
    """
    Проверяет, является ли число простым.

    :param number: Проверяемое число
    :return: True, если число простое, иначе False
    """
    if number <= 1:
        # Числа меньше или равные 1 не являются простыми
        return False
    elif number == 2:
        # 2 - единственное четное простое число
        return True
    elif number % 2 == 0:
        # Все другие четные числа не являются простыми
        return False
    else:
        # Проверяем делители от 3 до квадратного корня из числа
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
