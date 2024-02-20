"""
def fib(x):
    if x <= 1:
        print("value of x is", x)
        return x
    else:
        #print("value of x is", x)
        return fib(x-1) + fib(x-2)


num = int(input("enter the number of terms :"))
print("Fibonacci series :-")
for i in range(1, num):
    print(fib(i))
"""


def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


n_terms = int(input("enter the number of terms :"))
if n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n_terms):
        print(rec_fib(i))
