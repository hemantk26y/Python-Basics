# WAP to implement fibonacci series with recurrsion

def fibonacci(x):
    if x <= 1:
        #print("value of x is", x)
        return x
    else:
        #print("value of x is", x)
        return fibonacci(x - 1) + fibonacci(x - 2)


max_term = int(input("enter the number of terms to print fibonacci series :"))
if max_term <= 0:
    print("enter a positive number")
else:
    print("Fibonacci series generated as given :- ")
    for i in range(max_term):
        #print("value of 1 is", i)
        print(fibonacci(i))
