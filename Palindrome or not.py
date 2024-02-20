""" WAP to check whether a number is palindrome """

num = input("enter number in sequence :")
r_num = num[::-1]
if num == r_num:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")