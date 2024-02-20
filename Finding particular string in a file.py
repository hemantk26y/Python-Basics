# WAP to find particular string in a text file

f = input("enter the file name with extension :")
try:
    with open(f,"r") as f1:
        pa = input("enter a string to search :")
        ls = f1.read()
        wo = ls.split()
        if pa in ls:
            print("Found")
        else:
            print("Not Found")
except FileNotFoundError:
    print("File Not Exist")

