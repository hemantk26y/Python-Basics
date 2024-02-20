# WAP to find GCD of two number


num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
a = num1
b = num2
while b != 0:
    temp = b
    b = a % b
    a = temp

GCD = a
print("Print GCD of", num1, "and", num2, "is", GCD)
