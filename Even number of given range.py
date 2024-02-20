# WAP to find even numbers of a given range

e = int(input("enter the number up to which you want to print even number :"))
print("Even numbers up to", e)
for i in range(1, e + 1):
    if i % 2 == 0:
        print(i, ",", end=" ")
    else:
        pass
