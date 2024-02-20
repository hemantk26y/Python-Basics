# WAP to print Fabonacci Series

s = int(input("enter the number up to :"))
a = 0
b = 1
print(a)
print(b)
while s != 2:
    c = a+b
    print(c)
    a = b
    b = c
    s -= 1
