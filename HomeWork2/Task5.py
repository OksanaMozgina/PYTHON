#  Реализуйте алгоритм перемешивания списка.Без функции shuffle из модуля random.

from random import randrange

num = int(input("Enter the length of the list: "))
num_list = list(range(num))

print(num_list)

for i in range(num):
    num_1, num_2 = randrange(num), randrange(num)
    num_list[num_1], num_list[num_2] = num_list[num_2], num_list[num_1]

print(num_list)
