""" WAP to check whether a number is prime or not """
num = int(input("enter the number :"))
a = False
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            a = True
            break
if a:
    print(num, "This is not prime number")
else:
    print(num, "This is prime number")
