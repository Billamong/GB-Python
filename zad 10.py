n = int(input("Введите количество монет "))
Count1 = 0
Count0 = 0
for i in range(n):
    x=int(input("Введите 0 или 1 "))
    if x == 1:
        Count1 +=1
    if x == 0:
        Count0 +=1
if Count1<Count0:
    print(Count1)
else:
    print(Count0)