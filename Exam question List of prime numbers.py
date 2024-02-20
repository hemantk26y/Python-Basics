# WAP to print list of prime numbers within a specified range

lis = []
for i in range(1, 51):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
        else:
            pass
    if c == 2:
        lis.append(i)
print(lis)
