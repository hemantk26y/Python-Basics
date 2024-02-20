# WAP to input starting and ending number and print only those numbers which are not divisible by 5

s = int(input("enter the start :"))
e = int(input("enter the end :"))
while s <= e:
    if s % 5 == 0:
        pass
    else:
        print(s)
    s += 1
