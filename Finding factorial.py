# WAP to find factorial of a number

n = 3
nfac = 1
while n != 0:
    if n>0:
        nfac = nfac*n
        n = n-1
    elif n == 0:
        nfac = 1
print(nfac)