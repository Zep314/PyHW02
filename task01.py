# Задача 14. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

R = float(input("Введите вещественное число: "))
save = R
R = abs(R) # вдруг отрицательное введут

while not R.is_integer(): # делаем целое число из дробного
    R *= 10

summ = 0
while (R > 0):
    summ += R % 10 # считаем цифры
    R = R // 10

print(f'Сумма цифр числа {save} равна {int(summ)}')
