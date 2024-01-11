
def choice_size():
    size = input()
    while True:
        try:
            size = float(size)
            if size > 0:
                return size
            else:
                print('Размер должен быть положительным числом. Попробуйте еще раз.')
                size = input('Задайте размер снежинки: ')
        except ValueError:
            print('Размер задан неверно. Попробуйте еще раз.')
            size = input('Задайте размер снежинки: ')