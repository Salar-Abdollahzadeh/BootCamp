x = int(input('x is: '))
y = int(input('y is: '))


def divisible(x, y):
    return True if x % y == 0 else False


print(divisible(x, y))
