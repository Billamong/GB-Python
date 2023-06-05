# Черника

# kust = int(input("введите количество кустов: "))
# array = []
# result = 0
# i = 0
# sum = 0
# maxsum = 0
# for i in range(kust):
#     array.append(int(input(f"Введите количество ягод на {i+1} кусту : ")))
# print(array)

# while (i < kust):
#     if (i == 0):
#         sum = array[i] + array[kust - 1] + array[i + 1]
#     elif ( i == kust -1 ):
#         sum = array[0] + array[i] + array[i - 1]
#     else:
#         sum = array[i] + array[i - 1] + array[i + 1]

#     if maxsum < sum :
#         maxsum = sum
#     i += 1

# print(f"максимальное число ягод за одну итерацию {maxsum} ")

n = int(input())
array = [int(i) for i in input().split()][:n]
max_summa = 0
for i in range(1, len(array) - 1):
   if max_summa < array[i - 1] + array[i] + array[i + 1]:
      max_summa = array[i - 1] + array[i] + array[i + 1]

if max_summa < array[0] + array[1] + array[len(array) - 1]:
   max_summa = array[0] + array[1] + array[len(array) - 1]
if max_summa < array[0] + array[len(array) - 1] + array[len(array) - 2]:
   max_summa = array[0] + array[len(array) - 1] + array[len(array) - 2]
print(max_summa)