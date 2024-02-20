# WAP to count number of lines in a text file


f = input("enter the file name with extension :")
try:
    with open(f, "r") as f1:
        c = 0
        ls = f1.readlines()
        for i in ls:
            c += 1
        print(c)
except FileNotFoundError:
    print("File Not Exist")
