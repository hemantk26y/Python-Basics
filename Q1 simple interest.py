# WAP to calculate simple interest with function

def SI(p, r, t):
    si = (p * r * t) / 100
    a = p + si
    print(a)


p1 = int(input("enter the principal amount :"))
r1 = int(input("enter the rate of interest :"))
t1 = int(input("enter the time :"))
SI(p1, r1, t1)
