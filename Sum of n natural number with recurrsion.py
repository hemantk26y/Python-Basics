# WAP to sum n natural numbers with recurrsion

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)


n = int(input("enter the number :"))
print(sum(n))
