# WAP to print given pattern with  asterisk (*)
"""
    * 
    ** 
    ***
    ****
"""

r = int(input("enter the number of rows :"))
for i in range(1, r + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print(" ")
