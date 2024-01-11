
def choice_shape(shapes):
    for key, value in shapes.items():
        print(f'{key} - {value}')

    choice_shape = input('Ваш выбор: ')
    while choice_shape not in shapes.keys():
        print('Форма выбрана неверно. Попробуйте еще раз.')
        for key, value in shapes.items():
            print(f'{key} - {value}')

        choice_shape = input('Ваш выбор: ')
    
    return choice_shape