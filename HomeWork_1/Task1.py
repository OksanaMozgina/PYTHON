# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

num = int(input("Enter the number of the day of the week: "))
if 5 < num < 8:
    print("Weekend")
elif 0 < num < 6:
    print("Workday")
else:
    print("It's not a day of the week")
