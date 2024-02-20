# WAP to find real roots

import math


def findRoots(a, b, c):
    if a == 0:
        print("Invalid")
        return -1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))

    if d > 0:
        print("Roots are real and different ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    elif d == 0:
        print("Roots are real and same")
        print(-b / (2 * a))
    else:
        print("Roots are complex")
        print(- b / (2 * a), " + i", sqrt_val / (2 * a))
        print(- b / (2 * a), " - i", sqrt_val / (2 * a))


a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))
findRoots(a, b, c)
