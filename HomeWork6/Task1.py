# Представлен список чисел. 
# Необходимо вывести элементы исходного списка,
#  значения которых больше предыдущего элемента. 


from random import randrange

def list_rand_nums(count: int):
    if count < 0:
        print("Вы ввели отрицательное значение количества чисел!")
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums

def list_bigger_elem(list_nums: list):
    
    result = [list_nums[i] for i in range(1, len(list_nums)) if list_nums[i] > list_nums[i-1]] 
    return result

all_list = list_rand_nums(int(input("Введите длину списка: ")))
print(all_list)
print(list_bigger_elem(all_list))
