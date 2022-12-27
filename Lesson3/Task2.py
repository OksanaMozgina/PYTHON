# Задайте список, состоящий из произвольных слов, количество задает пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке дибо сообщит, что ее нет

from random import sample

def new_list (count, word = "abc"):
    my_list = []
    for i in range(count):
       temp = sample(word, k = 3)
       my_list.append("".join(temp))
    return my_list

def index_find(word,sum_list):
    if word in sum_list and sum_list.count(word) > 1:
        index_1 = sum_list.index(word)
        print(sum_list.index(word, index_1 + 1))  
    else:
        print(-1)

final_list = new_list(int(input())) 
print(final_list)
index_find(input(), final_list)
