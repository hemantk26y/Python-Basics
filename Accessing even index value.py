# WAP to access even index value of a tuple

t1 = (4, 6, 8, 9, 10, 12, 14, 15, 16, 17, 18, 20, 21)
print("Even index numbers with corresponding value")
for i in range(2, len(t1)):
    if i % 2 == 0:
        print("Value :", t1[i], " ", "Index number :", i)
