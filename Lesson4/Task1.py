# Задайте программу из набора чисел. Напишите программу, которая покажнт
# наибольшее и наименьшее число. В качестве разделителя используйте пробел

def user_input(user_str):
    new_str = user_str.split()
    lst = []

    for i in range(len(new_str)):
        new_str[i] = new_str[i].strip(",;.=!")
        if new_str[i].replace("-", "", 1).isdigit():
            lst.append(new_str[i])
    
    print(lst)

def user_output(lst):
    if lst:
        return max(lst, key=int), min(lst, key=int)
    return "Error"

print(user_output(user_input(input("..."))))
