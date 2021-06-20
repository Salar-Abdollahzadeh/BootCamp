import math

N = int(input("Number"))


def cal():
    x = math.pow(N, 4)*math.pi
    z = math.pow(x, 5)
    return z


print(cal())
