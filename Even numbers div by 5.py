# WAP to display even numbers divisible by 5

n = int(input("enter the upper limit :"))
print("Even numbers divisible by 5")
for i in range(1, n + 1):
    if i % 5 == 0:
        if i % 2 == 0:
            print(i)
