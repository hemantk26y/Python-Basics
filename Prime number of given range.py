# WAP to display prime numbers of given range

s = int(input("Enter the Start :"))
e = int(input("Enter the End :"))
print("Prime numbers between",s,"and",e)
for i in range(s, e + 1):
    c = 0
    for j in range(1,i+1):
        if i % j == 0:
            c += 1

    if c == 2:
        print(i)
    else:
        continue
