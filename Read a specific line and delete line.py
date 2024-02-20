# WAP to read specific line and delete

"""
with open("dummyfile1.txt", "r+") as f1:
    with open("dummyfile2.txt", "w") as f2:
        n = int(input("enter the number of line you want to read :"))
        ls = f1.readlines()
        print(ls[n - 1])

        n1 = int(input("enter the line want to delete :"))
        for i in ls:
            if n1 != n1:
                f2.write(i)
"""

f = input("enter the file name with extenstion :")

try:
    with open(f, "r") as f1:
        n = int(input("enter the number of line you want to read :"))
        ls = f1.readlines()
        print(ls[n - 1])
        ls = f1.readlines()
        count = 1
        with open(f, "w") as f2:
            delete = int(input("Enter the Number of Line you want to delete: "))
            for i in ls:
                if delete != count:
                    f2.write(i)
                count += 1
        print("Deleted")
except FileNotFoundError:
    print("File Not Exist")
