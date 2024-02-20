# WAP to display those value of a list which are divisible by 5

l1 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
print("Elements which are divisible by 5")
for i in l1:
    if i % 5 == 0:
        print(i)
