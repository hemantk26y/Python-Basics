# WAP to find sum of n natural numbers

n = int(input("enter the n :"))
i = 1
s = 0
while i <= n:
    s += i
    i += 1
print("The sum of n natural numbers :", s)
