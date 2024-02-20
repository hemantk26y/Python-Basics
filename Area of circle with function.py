# WAP to find area of circle with function

def AOC(radius):
    area = (22 / 7) * (radius ** 2)
    return area


r = float(input("Enter the Radius: "))
print("The Area of Circle (with radius", r, ") is: ", AOC(r))

