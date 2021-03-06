import random


def bubbles_sort(list):
    """
    Функция для сортировки с помощью метода пузырьков.Алгоритм состоит в повторяющихся проходах по
    сортируемому массиву, за каждый проход элементы последовательно сравниваются попарно
    и в случае необходимости выполняется обмен элементов.
    :param list: список неотсортированных элементов
    :return: список отсортированных элементов
    """
    N = len(list)
    R = N
    for i in range(0, R-1):  # i-номер прохода по списку, всплытие проводится для неотсортированной части
        for j in range(0, R-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]  # Обмен элементов
        R -= 1
    return list


def shell_sort(list):
    """
    Функция для сортировки с помощью метода Шелла. Сравнивает (и в случае неупорядоченности
    обменивать) не соседние элементы, а отстоящие друг от друга на некотором расстоянии d.
    На каждом шаге сортировки d уменьшается до тех пор,пока не станет равным 1.
    :param list: список неотсортированных элементов
    :return: список отсортированных элементов
    """
    N = len(list)
    d = int(N / 2)  # Расстояние сортировки
    while d > 0:
        for i in range(0, N - d):
            j = i
            while (j >= 0) and (list[j] > list[j + d]):
                list[j], list[j + d] = list[j + d], list[j]  # Обмен элементов
                j -= 1
            d -= 1
    return list


def quick_sort(list):
    """
    Функция для быстрой сортировки. Выбраем опорный элемент массива, разделяем массив на подмассивы:
    сравниваем остальные элементы с опорным и разбиваем массив на три подмассива: "меньшие опорного",
    "равные" и "большие", расположить их в порядке меньшие-равные-большие.
    Повторить рекурсивно для подмассивов "меньших" и "больших".
    :param list: список неотсортированных элементов
    :return: список отсортированных элементов
    """
    if len(list) <= 1:
        return(list)
    else:
        d = random.choice(list)
        a_nums = []
        b_nums = []
        c_nums = []
        for n in list:  # Сортировка с помощью добавления элементов в списки
            if n < d:
                a_nums.append(n)
            elif n > d:
                b_nums.append(n)
            else:
                c_nums.append(n)
        return quick_sort(a_nums) + c_nums + quick_sort(b_nums)
