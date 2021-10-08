def time(Hotp, Motp, Hp, Mp):  # Создаем функцию для нахождения значений
    hours_in_trip = (Hotp + Hp) % hours  # Находим часы прибытия
    days = Hp // hours  # Находим количество дней в пути

    if Motp + Mp < 60:
        minutes_in_trip = Motp + Mp  # Если сумма минут отправления и минут в пути меньше минут в часе, то складываем их
    else:
        minutes_in_trip = Motp + Mp - minutes  # Если сумма больше, то вычитаем количество минут в часе, чтоб найти минуты прибытия
        hours_in_trip += 1  # Прибавляем час к часам прибытия

# Выводим значения
    print(hours_in_trip, 'hours :', minutes_in_trip, 'minutes')
    print(days, 'days')


# Тело программы

hours = 24
minutes = 60

# Ввод значений
time(Hotp=int(input('Часы отправления: ')), Motp=int(input('Минуты отпрвления: ')), Hp=int(input('Часы в пути: ')), Mp=int(input('Минуты в пути: ')))
