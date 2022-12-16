# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

x_1 = int(input("Enter value x_1: "))
y_1 = int(input("Enter value y_1: "))
x_2 = int(input("Enter value x_2: "))
y_2 = int(input("Enter value y_1: "))

print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:0.4}")