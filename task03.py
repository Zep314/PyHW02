# Задача 16. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

size = int(input("Введите размер списка: "))

print(sum( [(1+1/n)**n for n in range(1,size+1)] ))
