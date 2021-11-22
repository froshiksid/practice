import math


def f(x):
    x = (x ** 4) - 10
    return x


def method(a, b, eps):  # Функция вычисления корня уравнения с помощью метода деления отрезков пополам
    if math.fabs(b - a) < eps:
        return (a + b) / 2
    else:
        x = (a + b) / 2
    if f(a) * f(x) <= 0:
        return str(method(a, x, eps))[:str(method(a, x, eps)).index('.') + count(eps)]
    else:
        return str(method(b, x, eps))[:str(method(b, x, eps)).index('.') + count(eps)]


def count(number):  # Функция, находящая количество знаков после запятой
    s = str(number)
    if '.' in s:
        return len(s[s.index('.'):])
