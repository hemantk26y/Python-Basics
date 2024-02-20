# WAP to remove user given value from set if find

s1 = {1, 2, 3, 4, 5, 6, 7, 8}
print("The set is: ", s1)
num = int(input("Enter the number you want to remove: "))
if num in s1:
    s1.remove(num)
print("Set after Removal: ", s1)
