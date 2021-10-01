# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9
print(type(number))   # Вывод типа переменной number

float_number = 9.0

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов

lenn = 2.4
snake = 4
stroch = "Площадь - произведение длины и ширины прямоугольника"

print(type(lenn))
print(type(snake))
print(type(stroch))

# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.

print(type(float(snake)))
print(type(int(lenn)))
print(type(str(lenn)))

print(int(float_number))
