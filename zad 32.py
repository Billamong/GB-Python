# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint as rd


min = int(input("Введите минимальный диапазон "))
max = int(input("Введите максимальный диапазон "))
list_1 = [rd(1, 11) for i in range(10)]

print(f'---------------------\nСписок 1: {list_1}\n------------------')
print( [int(min < list_1[i] < max) for i in range(10)])
# Не могу понять ка тут выводить именно индекс элементов


# list_2 = []
# for i in range(10):
#     if (min < list_1[i] < max):    # Это работает 
#         list_2.append(i)
# print(list_2)