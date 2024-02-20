# WAP to check value not exceed by 80

n1 = input("Enter the first number :")
n2 = input("Enter the second number :")
print("Length of {} is :".format(n1), len(n1))
print("Length of {} is :".format(n2), len(n2))
if len(n1) < 80 or len(n2)<80:
    print("Sum of {} and {}".format(n1, n2), int(n1) + int(n2))
else:
    print("length of variable exceeds")
