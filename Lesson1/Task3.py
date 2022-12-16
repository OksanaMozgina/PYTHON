#Напишите программу , которая на вход будет принимать дробь 
#и показывать первую цифру дробной части числа
number = float(input("Input your number : "))
new_num = int(number * 10 % 10)
print(new_num)
