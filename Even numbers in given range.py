# WAP to input starting and ending number and print all the even numbers  between them

s = int(input("enter the start :"))
e = int(input("enter the end :"))
while s <= e:
    if s % 2 == 0:
        print(s)
    s += 1
