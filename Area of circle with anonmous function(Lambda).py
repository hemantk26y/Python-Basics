# WAP to find area of circle with lambda function

r = float(input("Enter the radius of the circle: "))
area = lambda radius: (22 / 7) * (radius ** 2)
print("Area of Circle is", area(r))
