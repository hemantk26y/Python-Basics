# =============== Swapping of Values =================

a1 = int(input("enter a digit (0 to 9) : "))
a2 = int(input("enter a digit (0 to 9) : "))
c = int(input("enter your choice for swapping ( 1: for with third variable or 2: for without third variable) :"))
print("Before Swapping :", a1, a2)
if c == 1:
    r = a1
    a1 = a2
    a2 = r
    print("After Swapping ", a1, a2)
elif c == 2:
    a1, a2 = a2, a1
    print("After Swapping ", a1, a2)
else:
    print("You have entered a wrong choice")

