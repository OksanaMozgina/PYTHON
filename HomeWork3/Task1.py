# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).

from random import sample

def list_rand(count: int):
    if count < 0:
        print(" Negativ value of the number of numbers")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums

def sum_od_pos(list_nums: list):
    sum_nums = 0
    for k in range(0, len(list_nums), 2):
        sum_nums += list_nums[k]
    return sum_nums

all_list = list_rand(int(input("Number of numbers: ")))
print(all_list)
print(sum_od_pos(all_list))
