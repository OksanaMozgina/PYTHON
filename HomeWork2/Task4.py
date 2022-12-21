# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

num  = int(input("Enter the value of N: "))
num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))

num_list = list(range(-num, num + 1))

print(num_list)
len_list = len(num_list)

if len_list >= num_1 > 0 and len_list >= num_2 > 0:
    print(num_list[num_1 - 1] * num_list[num_2 - 1])
