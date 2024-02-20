# ======== WAP to find the greatest of 3 numbers inputted by the user ==========

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))

if (a > b) and (a > c):
    print(a, "is greatest of 3 numbers")
elif (b > a) and (b > c):
    print(b, "is greatest of 3 numbers")
else:
    print(c, "is greatest of 3 numbers")
