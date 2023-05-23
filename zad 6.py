
n= int(input("Введите номер билета "))
m1 = n % 10
n = n // 10
m2 = n % 10
n = n // 10
m3 = n % 10
n = n // 10
m4 = n % 10
n = n // 10
m5 = n % 10
n = n // 10
m6 = n % 10
n = n // 10
t1 = m1+m2+m3
t2 = m4+m5+m6
if t1==t2:
    print("Yes")
else:
    print("No")