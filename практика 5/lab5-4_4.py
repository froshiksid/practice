# Функция для нахождения путей, по которым будем склонять слова


def counter(money, way_1, way_2, way_3):
    pennies = pennies_1 % 10
    if 5 <= pennies <= 20:
        return way_1
    elif pennies == 1:
        return way_2
    else:
        return way_3


# Тело программы

amount = int(input('Введите сумму покупки (от 1 до 100 000): '))
rubles = amount // 100  # Нахождим рубли
pennies_1 = amount % 100  # Находим копейки

# Условия, по которым происходит вывод значений и склонение слов "рубль", "копейка
if rubles > 0 and pennies_1 > 0:
    print(f'{rubles} {counter(rubles, "рублей", "рубль", "рубля").upper()}')
    print(f'{pennies_1} {counter(pennies_1, "копеек", "копейка", "копейки").upper()}')
elif rubles > 0:
    print(f'{rubles} {counter(rubles, "рублей", "рубль", "рубля").upper()}')
elif pennies_1 > 0:
    print(f'{pennies_1} {counter(pennies_1, "копеек", "копейка", "копейки").upper()}')
