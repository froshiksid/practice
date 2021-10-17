import os
from prime_numbers import prime_numbers

if os.path.exists('D:/МОЕ/универ/программирование/практика 6/input4.txt'):  # проверка существования файла
    file = open('input4.txt', 'r')
    Number = int(file.readline())
    prime_numbers(Number)

else:  # если файл с исходными данными не существует, то пишем об этом
    file = open('output4.txt', 'w')
    file.write('Файл с входными данными не обнаружен')
    file.close()
