import os
if os.path.exists('D:/МОЕ/универ/программирование/практика 6/input3.txt'):  # проверка существования файла
    file = open('input3.txt', 'r')
    Number = file.readline()
    Sum = 0
    composition = 1
    file.close()

    for i in range(len(Number)):
        figures = [int(a) for a in str(Number)]

    for i in figures:
        Sum += i  # находим сумму цифр
        composition *= i  # находим произведение цифр

# выводим необходимые значения в файл

    file = open('output3.txt', 'w')
    file.write('Число: ' + str(Number) + '\n')
    file.write('Количество цифр: ' + str(len(Number)) + '\n')
    file.write('Сумма цифр: ' + str(Sum) + '\n')
    file.write('Произведение цифр: ' + str(composition))
    file.close()

else:  # если файл с исходными данными не существует, то пишем об этом
    file = open('output3.txt', 'w')
    file.write('Файл с входными данными не обнаружен')
    file.close()
