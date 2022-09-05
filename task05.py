# Задача 18. Реализуйте алгоритм перемешивания списка.

from random import randint

def my_shuffle(local_list): # перемешиваем список
    for i in range(0, len(local_list) - 1):
        pos = randint(i, len(local_list) - 1)
        local_list[i], local_list[pos] = local_list[pos], local_list[i]
    return local_list

size = int(input("Введите размер списка: "))

# Создаем последовательный список
my_list = [_ for _ in range(0,size)]

print("Список до перемешивания")
print(my_list)

print("Список после перемешивания")
print(my_shuffle(my_list))

