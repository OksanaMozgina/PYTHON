# Напишите программу, которая принимает на входвещественное число и показывает сумму его цифр.
# Без работы с методами строк.

num = input("Input your number: ")
sum_digits = 0

power = len(num) - 2
num = float(num)
num *= int(10 ** power)

while num:
    sum_digits += int(num % 10)
    num //= 10

print(int(sum_digits))