"""Арифметические операции учебного калькулятора."""


def add(a: float, b: float) -> float:
    """Возвращает сумму a и b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Возвращает разность a и b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Возвращает произведение a и b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Возвращает частное a и b."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b


def power(base: float, exponent: int) -> float:
    """Возводит base в целую степень exponent без использования оператора **."""
    if not isinstance(exponent, int):
        raise TypeError("Показатель степени должен быть целым числом")
    result = 1.0
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result


def factorial(n: int) -> int:
    """Возвращает факториал неотрицательного целого числа."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result