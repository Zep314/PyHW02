# Задача 17. Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в однойстроке одно число.


from random import randint

my_filename= "file.txt"
N=int(input("Задайте N: "))

# Задаем список случайных чисел
my_list = [randint(-N,N) for _ in range(N)]

print("Список:")
print(my_list)

# Работаем с файлом
with open(my_filename,'r') as f:
    file_context =list(map(int,f.readlines())) # читаем в строку -
                                               # и каждую прочитанную строку обращаем в int
print("Позиции элементов списка, которые надо перемножить:")
print(file_context)

list_to_multiple = [my_list[i] for i in file_context]
print("Список для перемножения:")
print(list_to_multiple)
res = 1
for i in list_to_multiple:
    res *= i
print(f'Результат перемножения списка: {res}')
