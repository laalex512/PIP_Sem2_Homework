# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input("Insert Num: ")
sum = 0
for i in range(len(num)):

    if (num[i] != ",") and (num[i] != "."):
        sum += int(num[i])


print(sum)
