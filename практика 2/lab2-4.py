# Составной оператор присваивания объединяет в себе простое присваивание и арифметическую бинарную операцию (+=, -= и т.д).

number = 9.0

print("number = " + str(number))

number -= 2

print("number = " + str(number))

# Попрактикуйтесь в использовании разных типов составных операторов для переменной number, выведите результаты в консоль

number += 5
print("number = " + str(number))

n = 0
while number < 100:
    number *= 1.5
    n += 1
print(n, number)
