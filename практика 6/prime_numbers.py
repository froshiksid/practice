def prime_numbers(n):  # функция, проверяющая простоту числа и выводящая число в файл
    file = open('output4.txt', 'w')

    for number in range(2, n):
        prime_number = True

# проверяем число на простоту: если остаток от деления 0, то составное, если нет, то простое

        for i in range(2, number):
            if number % i == 0:
                prime_number = False
        if prime_number:
            numbers = str(number)
            file.write(numbers + ' ')  # Вывод чисел через пробел

    file.close()
