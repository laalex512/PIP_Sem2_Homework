# Task 14
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = input("Insert Num: ")
# sum = 0
# for i in range(len(num)):
#     if (num[i] != ",") and (num[i] != "."):
#         sum += int(num[i])
# print(sum)


# Task 15
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input("Insert N: "))
# resultList = [None]*num
# resultList[0] = 1
# for i in range(1, num):
#     resultList[i] = resultList[i-1]*(i+1)
# print(resultList)


# Task 16
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.

def ourFunc(x):
    return (1+1/x)**x


num = int(input("Insert n: "))
sum = 0
for i in range(1, num+1):
    sum += ourFunc(i)
print(sum)
