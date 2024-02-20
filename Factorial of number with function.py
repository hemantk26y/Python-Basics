# WAP to find factorial of any number with the help of function

n = int(input("Enter the number :"))


def Fac(num):
    fac = 1
    if num == 0:
        print("Factorial of 0 is", 1)
    elif num > 0:
        while num >= 1:
            fac = fac * num
            num = num - 1

    else:
        print("Invalid number")
    print("Factorial of given number :", fac)


# Fac(n)


def fac_term(num):
    if (num == 1) or (num == 0):
        return num
    else:
        return num * fac_term(num - 1)
print("Factorial of",n,"is",fac_term(n))
