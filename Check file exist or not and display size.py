# WAP to check file exist or not and display it's size

f = input("enter the file name with extension :")

try:
    with open(f,"r") as f1:
        c = 0
        ob = f1.read()
        l = len(ob)
        print(l)
except FileNotFoundError:
    print("File Not Exist")


