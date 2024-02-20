# WAP between 1 to 50

lower = 1
upper = 50
print("Prime numbers between", lower, "and", upper)
for i in range(lower, upper + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
