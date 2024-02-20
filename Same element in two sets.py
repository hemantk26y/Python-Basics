# WAP to list out element are same in given two sets

def com_elm(s1, s2):
    c = 0
    for i in s1:
        for j in s2:
            if i == j:
                print(i)
                c += 1
    if c == 0:
        print("No Same Items in the Sets")
    else:
        print("These elements are same in both Sets")


set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 3, 5, 7, 9, 11, 13, 15,17}
print("First set: ", set1)
print("Second set: ", set2)
com_elm(set1, set2)
