# WAP to input a number from user and print table of that number

a = int(input("Enter for which you want to display the table : "))
i = 1
while i <= 10:
    print(a, "*", i, "=", a * i)
    i += 1
