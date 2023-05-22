n= int(input("Введите 3-х значное число "))
m = n % 10
n = n // 10
v = n % 10
n = n // 10
f = n % 10
rezul = m+v+f
print(rezul)