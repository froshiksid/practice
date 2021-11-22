def reading():  # Функция для чтения значений
    f = open('input.txt', 'r')
    numbers = f.readline().split()
    f.close()
    return numbers


answer = []  # Один из вариантов решения задачи - использование глобальной переменной (список)


def main_function(numbers, element=0):  # Функция для сортировки значений в список (сначала отрицательные, потом положительные)
    global answer
    if int(numbers[element]) > 0:
        answer.append(numbers[element])
        main_function(numbers, element + 1)
    elif int(numbers[element]) < 0:
        answer.insert(0, numbers[element])
        main_function(numbers, element + 1)
    return answer


def writing(ans):  # Функция для вывода списка в файл
    f = open('output.txt', 'w')
    for an in ans:
        f.write(an + ' ')
    f.close()
