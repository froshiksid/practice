import math

# Вводдим вещественные коэффициенты с клавиатуры

A = float(input("Введите коэффициент A: "))
B = float(input("Введите коэффициент B: "))
C = float(input("Введите коэффициент C: "))


def discriminant(a, b, c):  # Функция для нахождения дискриминанта
    desc = (B ** 2) - 4 * A * C
    return desc


def equation():  # Функция для печати уравнения
    print("Уравнение", '(%.5f)*X^2+(%.5f)+(%.5f)=0' % (A, B, C), sep='\n')


def formatting(number):  # Функция для форматирования и вывода корней уравнения
    print(format(number, '.5f'))


# Тело программы

if A == 0:  # Находим, существует ли квадратное уравнение
    print("Коэффициент A не может быть равен 0!")
# Убедившись, что уравнение существует, находим количество корней и их значения
elif discriminant(A, B, C) > 0:  # Рассматриваем случай, когда дискриминант больше 0 и корня 2
    equation()
    x1 = (-B + math.sqrt(discriminant(A, B, C))) / (2 * A)
    x2 = (-B - math.sqrt(discriminant(A, B, C))) / (2 * A)
    print("Количество корней: 2")

    if x1 > x2:
        formatting(x2)
        formatting(x1)
    else:
        formatting(x1)
        formatting(x2)

elif discriminant(A, B, C) == 0:  # Рассматриваем случай, когда дискриминант равен 0 и получаются два совпадающих корня
    equation()
    print("Количество корней: 1")
    x1 = x2 = -B / (2 * A)
    formatting(x1)
    formatting(x2)
else:  # Рассматриваем случай, когда дискриминант меньше 0
    equation()
    print("Количество корней: 0")
