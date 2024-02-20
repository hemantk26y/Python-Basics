# WAP to find prime number between 1 to any given number

r = int(input("Enter the range up to which you want prime numbers :"))
print("Following are the prime number between ", 1, "and", r, "are")
for i in range(1, r + 1):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
        else:
            continue
    if c == 2:
        print(i)
