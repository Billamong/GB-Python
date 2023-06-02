

n1 = int(input('Введите длинну первого массива: '))
n2 = int(input('Введите длинну второго массива: '))
array1 = []
array2 = []
array3 = []
for i in range(n1):
    array1.append(int(input('Введите элемент первого массива: ')))
for j in range(n2):
    array2.append(int(input('Введите элемент второго массива: ')))

for i in array1:
    if i in array2: #and i not in array3:
            array3.append(i)
print(array3)