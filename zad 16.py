
n = int( input('Введите размер массива: '))
list_1 = input('Введите элементы массива: ').split()
array = list(map(int, list_1))
x = int( input('Введите искомый элемент: '))
count = 0

for i in range(n):
    if array[i] == x:
        count += 1

print(f'Число {x} встречается {count} раз.')



