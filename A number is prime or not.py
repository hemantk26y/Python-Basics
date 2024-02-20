""" WAP to check whether a number is prime or not """

num = int(input("Enter the number :"))
c = 0
for i in range(1, num + 1):
    if num % i == 0:
        c += 1

if c == 2:
    print(num,"is a prime number")
else:
    print(num, "is not a prime number")