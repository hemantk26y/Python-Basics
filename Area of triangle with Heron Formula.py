# WAP to find area of triangle with Heron's Formula


def AOT(side1, side2, side3):
    s_p = (side1 + side2 + side3) / 2
    area = (s_p * (s_p - side1) * (s_p - side2) * (s_p - side3)) ** 0.5
    return area


s1 = float(input("Enter the first side: "))
s2 = float(input("Enter the second side: "))
s3 = float(input("Enter the third side: "))

print("The Area of Triangle (with sides", s1, s2, "and", s3, ") is: ", AOT(s1, s2, s3))
