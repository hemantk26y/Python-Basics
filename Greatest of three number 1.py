""" Find the greatest of 3 numbers """

a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))

if a > b:
    if a > c:
        print(a, "is the greatest of three number")
    else:
        pass
elif b > a:
    if b > c:
        print(b, "is the greatest of three number")
    else:
        pass
else:
    print(c, "is the greatest of three number")
