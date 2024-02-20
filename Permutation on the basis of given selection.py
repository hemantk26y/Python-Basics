# WAP to find permutation based on given selection

l1 = [1,2,3,4,5]
l = 0
for i in l1:
    l += 1
print(l)
n = l
r = int(input("number of objects selected :"))
if r <= l:
    n_r = l-r
    n_fac = 1
    n_r_fac = 1
    while n != 0:
        if n == 0:
            n_fac = 1
        elif n > 0:
            n_fac *= n
            n = n-1
        else:
            print("invalid value")
    while n_r != 0:
        if n_r == 0:
            n_r_fac = 1
        elif n_r > 0:
            n_r_fac *= n_r
            n_r = n_r - 1
        else:
            print("invalid value")
    per = n_fac/n_r_fac
    print(per)
else:
    print("r should be greater than n")