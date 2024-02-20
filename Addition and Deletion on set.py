# WAP to perform addition and deletion on set

s1 = {1, 2, 3, 4, 5}
print("To add : 1, To remove : 2")
ch = int(input("enter your choice :"))
if ch == 1:
    print("Before Add", s1)
    a = int(input("enter the number you want to add :"))
    s1.add(a)
    print("After Add", s1)
elif ch == 2:
    print("Before Remove", s1)
    a = int(input("enter the number you want to remove :"))
    s1.remove(a)
    print("After Remove", s1)
