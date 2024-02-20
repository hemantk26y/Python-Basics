# ================== Finding roots of the quadratic equation =================

a = int(input("coefficient of x square (a) : "))
b = int(input("coefficient of x (b) : "))
c = int(input("constant (c) : "))

d = (b ** 2) - (4 * a * c)
d1 = d ** (1 / 2)
sum_r = -b/a
pro_r = c/a
print("Sum of roots (alpha + beta) :", sum_r)
print("Product of roots (alpha * beta) :", pro_r)
print("Determinant of quadratic equation is :", d)

if d >= 0:
    r1 = (-b/(2*a))
    r2 = (-b/(2*a))
    r = (d1 / (2 * a))
    print("Solutions are :-\n", "alpha :", r1+r, "\n", "beta :", r2-r)
else:
    print("This equation have no real roots")
