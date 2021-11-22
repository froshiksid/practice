import os


def reading():  # Функция для чтения значений
    f = open('input.txt', 'r')
    numbers = f.readline().split()
    f.close()
    return numbers


def main_function(numbers, element=0):  # Функция для сортировки элементов в два вспомогательных файла
    if int(numbers[element]) > 0:
        f = open('positive.txt', 'a+')
        f.write(numbers[element] + ' ')
        f.close()
        main_function(numbers, element + 1)
    elif int(numbers[element]) < 0:
        f = open('negative.txt', 'a+')
        f.write(numbers[element] + ' ')
        f.close()
        main_function(numbers, element + 1)


def writing():  # Функция для удаления вспомогательных файлов и вывода значений
    f = open('negative.txt')
    numbers_1 = str(f.readline())
    f.close()
    os.remove('D:/МОЕ/Универ/Программирование/практика 7/negative.txt')
    f = open('positive.txt')
    numbers_2 = str(f.readline())
    f.close()
    os.remove('D:/МОЕ/Универ/Программирование/практика 7/positive.txt')
    f = open('output.txt', 'w')
    f.write(numbers_1 + numbers_2)
    f.close()
