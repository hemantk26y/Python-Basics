""" WAP to check whether the string is palindrome """
s = input("enter the string :")
r = s[::-1]
if s == r:
    print("The string is palindrome")
    print(s, " ", r)
