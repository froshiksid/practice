def print_square(a):  # Функция для печати квадрата с заданной стороной
    file = open('output2.txt', 'w')
    file.write('* ' * a + '\n')
    for i in range(a-2):
        file.write('*' + ' ' * (2 * a - 3) + '*' + '\n')
    file.write('* ' * a)
    file.close()


def print_rectangle(x, y): # Функция для прямоугольника квадрата с заданными сторонами
    file = open('out2.txt', 'w')
    file.write('* ' * x + '\n')
    for i in range(y-2):
        file.write('*' + ' ' * (2 * x - 3) + '*' + '\n')
    file.write('* ' * x)
    file.close()
