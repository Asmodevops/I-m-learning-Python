import pytest
from is_prime import is_prime

def test_prime_numbers():
    # Проверка, что простые числа возвращают True
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in primes:
        assert is_prime(num) is True

def test_non_prime_numbers():
    # Проверка, что не простые числа возвращают False
    non_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 20]
    for num in non_primes:
        assert is_prime(num) is False

def test_negative_number():
    # Проверка, что отрицательные числа не являются простыми
    negative_numbers = [-2, -3, -5, -7, -11, -13, -17, -19, -23, -29]
    for num in negative_numbers:
        assert is_prime(num) is False

def test_zero_and_one():
    # Проверка, что 0 и 1 не являются простыми числами
    assert is_prime(0) is False
    assert is_prime(1) is False

def test_large_prime():
    # Проверка для большого простого числа
    large_prime = 999983  # простое число, ближайшее к 1000000
    assert is_prime(large_prime) is True

def test_large_non_prime():
    # Проверка для большого не простого числа
    large_non_prime = 999980  # 2 * 2 * 5 * 49999
    assert is_prime(large_non_prime) is False