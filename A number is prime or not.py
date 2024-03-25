# WAP to check whether a number is prime or not

number = int(input("Enter the number to check :"))
count = 0
for num in range(1, number + 1):
    if number % num == 0:
        count += 1

if count == 2:
    print(num,"is a prime number")
else:
    print(num, "is not a prime number")
