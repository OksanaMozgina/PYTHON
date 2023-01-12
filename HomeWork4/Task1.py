# Вычислить число c заданной точностью d
# in
# Enter a real number: 9
#Enter the required accuracy '0.0001': 0.000001
# out 9.000000

from decimal import Decimal, getcontext

number = Decimal(input("Введите число : "))

accuracy = Decimal(input("Введите требуемую точность '0.0001 : "))

def num_accuracy(n, a):
    print("Число с заданной точностью : ", n.quantize(a))

num_accuracy(number, accuracy)
