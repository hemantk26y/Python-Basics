# WAP to find permutation of selected objects

l1 = [1, 2, 3]
n = len(l1)
r = int(input("enter the number of objects selected :"))
r_fac = 1
n_fac = 1
n_r = n - r
n_r_fac = 1

print("To find Combination : 1, To find Permutation : 2")
ch = int(input("enter your choice :"))
if ch == 1:
    while n >= 0:
        if n == 0:
            n_fac = 1
            r_fac = 1
            n_r_fac = 1
        else:
            n_fac *= n
            r_fac *= r
            n_r_fac *= n_r
            n = n - 1
            r = r - 1
    com = n_fac/r_fac*n_r_fac
    print(com)
elif ch == 2:
    while n >= 0:
        if n == 0:
            n_fac
            n_fac *= n
            n_r_fac *= n_r
            n = n - 1
    per = n_fac/n_r_fac
    print(per)
else:
    print("Invalid Input")