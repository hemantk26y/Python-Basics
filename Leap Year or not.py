# WAP to find whether a year entered by user is a leap year or not

y = int(input("Enter any year : "))

if (y % 400 == 0) and (y % 100 == 0):
    print(y, "is a leap year")
elif (y % 4 == 0) and (y % 100 != 0):
    print(y, "is a leap year")
else:
    print(y, "is not a leap year")
