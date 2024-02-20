# WAP to find the difference between values at even and odd position

n = int(input("Enter the number :"))
st = str(n)
s_e = 0
s_o = 0
for i in range(len(st)):
    if i % 2 == 0:
        s_o += int(st[i])
    else:
        s_e += int(st[i])
if s_e > s_o:
    diff = s_e - s_o
    print("Difference Between Sum of even number and odd number :", diff)
else:
    diff = s_o - s_e
    print("Difference Between Sum of even number and odd number :", diff)
