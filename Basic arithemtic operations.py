# WAP to perform basic arithemtic operations

x = int(input("Enter the 1st number : "))
y = int(input("Enter the 2nd number : "))
op = int(input("Enter the operation you want to perform : add - 1, sub - 2, multi - 3, div - 4 : "))
if op == 1:
    print(x+y)
elif op == 2:
    print(x-y)
elif op == 3:
    print(x*y)
elif op == 4:
    print(x/y)
else:
    print("Invalid Input")
