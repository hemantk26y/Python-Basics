# WAP to implement calcualtion with recurrsion

def calc(op):
    def add():
        ans = "Y"
        num = int(input("enter the number :"))
        r = num
        while ans:
            num = int(input("enter the number :"))
            r += num
            ans = input("Do you want to enter more number..?(Y or N)")
            if ans == "N" or ans == "n":
                break
        print(r)
        ans = input("Do you want to run this again...?(Y or N) ")
        if ans == "Y" or ans == "y":
            print("Add : 1, Sub : 2, Multi : 3, Div : 4")
            op = int(input("enter your choice :"))
            calc(op)
    def sub():
        ans = "Y"
        num = int(input("enter the number :"))
        r = num
        while ans:
            num = int(input("enter the number :"))
            r -= num
            ans = input("Do you want to enter more number..?(Y or N)")
            if ans == "N" or ans == "n":
                break
        print(r)
        ans = input("Do you want to run this again...?(Y or N) ")
        if ans == "Y" or ans == "y":
            print("Add : 1, Sub : 2, Multi : 3, Div : 4")
            op = int(input("enter your choice :"))
            calc(op)
    def multi():
        ans = "Y"
        num = int(input("enter the number :"))
        r = num
        while ans:
            num = int(input("enter the number :"))
            r *= num
            ans = input("Do you want to enter more number..?(Y or N)")
            if ans == "N" or ans == "n":
                break
        print(r)
        ans = input("Do you want to run this again...?(Y or N) ")
        if ans == "Y" or ans == "y":
            print("Add : 1, Sub : 2, Multi : 3, Div : 4")
            op = int(input("enter your choice :"))
            calc(op)
    def div():
        ans = "Y"
        num = int(input("enter the number :"))
        r = num
        while ans:
            num = int(input("enter the number :"))
            r /= num
            ans = input("Do you want to enter more number..?(Y or N)")
            if ans == "N" or ans == "n":
                break
        print(r)
        ans = input("Do you want to run this again...?(Y or N) ")
        if ans == "Y" or ans == "y":
            print("Add : 1, Sub : 2, Multi : 3, Div : 4")
            op = int(input("enter your choice :"))
            calc(op)
    if op == 1:
        add()
    elif op == 2:
        sub()
    elif op == 3:
        multi()
    elif op == 4:
        div()
    else:
        print("invalid input")
print("Add : 1, Sub : 2, Multi : 3, Div : 4")
op = int(input("enter your choice :"))
calc(op)


