# WAP to find sum of n natural numbers

n = int(input("enter the no. up to which want sum of natural no. :"))
s = 0
for i in range(1, n + 1):
    s += i
print(s)
