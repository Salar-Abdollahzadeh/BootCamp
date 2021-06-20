number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : '))


def max_mun(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        max_mun = num1
    elif (num2 > num1) and (num2 > num3):
        max_mun = num2
    else:
        max_mun = num3
    print("max is : ", max_mun)


def min_num(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        min_num = num1
    elif (num2 < num1) and (num2 < num3):
        min_num = num2
    else:
        min_num = num3
    print("min is : ", min_num)


max_mun(number1, number2, number3)
min_num(number1, number2, number3)
