n = int(input("Введите число N "))
P = 2
for i in range(n):
    P = P ** i
    if P <= n:
        print(P, end=' ')
        P = 2