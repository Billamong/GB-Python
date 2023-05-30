n = int(input('Введите количество элементов массива : '))
Ai = [i for i in range(1, n+1)]
X = int(input('Введите число X: '))
A= list(map(int, Ai))
b = X - A[0]
index = 0
print(Ai)
for i in range(1, n):
    count = X - A[i]
    if count < b:
        b = count
        index = i
print(f'Самое близкое чиcло это: {A[index]}')