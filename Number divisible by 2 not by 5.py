# WAP to input starting and ending number and display number that are divisible by 2 but not by 5

s = int(input("enter the start :"))
e = int(input("enter the end :"))
while s <= e:
    if s % 2 == 0:
        if s % 5 != 0:
            print(s)
    s += 1
