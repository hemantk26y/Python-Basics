""" WAP to find total and average marks """

l = []
ans = "Y"
while True:
    name = input("enter student name :")
    sub = []
    for i in range(1, 4):
        sub_name = input("enter the subject name(Theory) :")
        sub_marks = int(input("enter subject marks(Theory) :"))
        sub1 = [sub_name, sub_marks]
        sub.append(sub1)
    for i in range(1, 5):
        sub_name = input("enter the subject name(Practical) :")
        sub_marks = int(input("enter subject marks(Practical) :"))
        sub1 = [sub_name, sub_marks]
        sub.append(sub1)
    t_marks = 0
    for i in range(len(sub) - 1):
        t_marks += sub[i][1]
    per = (t_marks / 7)
    l1 = [name, sub, t_marks, per]
    l.append(l1)
    ans = input("Do you want to enter more records...? (Y/N) ")
    if ans == "N" or ans == "n":
        break

#for i in range(len(l)-1):

print(l)