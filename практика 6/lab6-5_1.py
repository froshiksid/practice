import os
from Rectangle_square import print_square
from Rectangle_square import print_rectangle

if os.path.exists('D:/МОЕ/универ/программирование/практика 6/input2_1.txt'):  # проверка существования файла
    file = open('input2_1.txt', 'r')
    x, y = map(int, file.readline().split())  # считывание значений сторон
    print_rectangle(x, y)  # вызов функции
    file.close()
else:
    f = open('out2.txt', 'w')
    f.write('Файл с входными данными не обнаружен')
    f.close()

if os.path.exists('D:/МОЕ/универ/программирование/практика 6/input2_2.txt'):  # проверка существования файла
    file = open('input2_2.txt', 'r')
    a = int(file.readline())  # считывание значения стороны
    print_square(a)  # вызов функции
else:
    f = open('output2.txt', 'w')
    f.write('Файл с входными данными не обнаружен')
    f.close()
