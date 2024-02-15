import pytest
from calculate_average import calculate_average

def test_valid_numbers():
    # Проверка среднего значения для валидных чисел
    numbers = [1, 2, 3, 4, 5]
    result = calculate_average(numbers)
    assert result == 3.0

def test_empty_list():
    # Проверка, что функция вызывает ValueError при пустом списке
    with pytest.raises(ValueError):
        calculate_average([])

def test_float_numbers():
    # Проверка среднего значения для списка с дробными числами
    numbers = [1.5, 2.5, 3.5, 4.5]
    result = calculate_average(numbers)
    assert result == 3

def test_negative_numbers():
    # Проверка среднего значения для списка с отрицательными числами
    numbers = [-1, -2, -3, -4, -5]
    result = calculate_average(numbers)
    assert result == -3.0

def test_mixed_numbers():
    # Проверка среднего значения для списка с разными типами чисел
    numbers = [1, 2.5, -3, 4.5, -5]
    result = calculate_average(numbers)
    assert result == 0


