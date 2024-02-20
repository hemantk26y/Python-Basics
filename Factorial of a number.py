# WAP to find factorial of a number

num = int(input("enter the number to find factorial :"))

fac = 1
while num != 0:
    if num == 0:
        print("Factorial of", num, " is", 1)
    else:
        fac *= num
    num -= 1
print("Factorial of", num, " is",fac)
