""" write a program to input the sides of triangle from user and decide whether the triangle is equilateral, isosceles
or scalene """
a = int(input("Enter the 1st side : "))
b = int(input("Enter the 2nd side : "))
c = int(input("Enter the 3rd side : "))

if (a == b) and (a == c):
    print("Equilateral")
elif (a != b) and (a != c) and (b != c):
    print("Scalene")
else:
    print("Isosceles")
