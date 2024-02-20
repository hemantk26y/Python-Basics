# WAP to check overflow (sum of two given integer should not be greater than 80)

def Overflow(num1, num2):
    s = num1 + num2
    if s >= 0:
        if s < 80:
            print("Sum of two integers", s)
        else:
            print("overflow")


n1 = int(input("enter the 1st number :"))
n2 = int(input("enter the 2nd number :"))
Overflow(n1, n2)
