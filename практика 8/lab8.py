import sorts
from prettytable import PrettyTable
import random
from datetime import datetime
import check


N = int(input('Введите количество элементов последовательности: '))
list = []
for i in range(N):  # Создание рандомной последовательности с определенным кол-вом элементов
    list.append(random.randint(-100000, 100000))


def time(list):
    start = datetime.now().timestamp()
    sorts.bubbles_sort(list)
    time_1 = str(round(datetime.now().timestamp() - start, 3))

    start = datetime.now().timestamp()
    sorts.shell_sort(list)
    time_2 = str(round(datetime.now().timestamp() - start, 3))

    start = datetime.now().timestamp()
    sorts.quick_sort(list)
    time_3 = str(round(datetime.now().timestamp() - start, 3))

    return time_1, time_2, time_3


time_1, time_2, time_3 = time(list)  # Время случайно отсортированной последовательности
list.sort()
time_12, time_22, time_32 = time(list)  # Время отсортированной последовательности
list.reverse()
time_13, time_23, time_33 = time(list)  # Время отсортированная в обратном порядке последовательности

# Заполняем таблицу

table = PrettyTable()
table.field_names = ['Метод', 'Отсортированная', 'Случайная', 'Отсортированная в обратном порядке']
table.add_row(['Метод пузырька', time_12, time_1, time_13])
table.add_row(['Метод Шелла', time_22, time_2, time_23])
table.add_row(['Быстрая сортировка', time_32, time_3, time_33])

# Переносим данные в файл

file = open('output.txt', 'w')
text = table.get_string()
file.write(str(check.check(list)) + '\n')
file.write('Число элементов последовательностей: ' + str(N) + '\n')
file.write(text)
file.close()
