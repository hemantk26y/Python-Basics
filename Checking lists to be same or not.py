# WAP to check whether two given lists are same or not


l1 = []
l2 = []
n = int(input("Enter the number of element you want to enter :"))
for i in range(n):
    elm1 = int(input("Enter the element in list 1 :"))
    elm2 = int(input("Enter the element in list 2 :"))
    l1.append(elm1)
    l2.append(elm2)
print("List 1", l1)
print("list 2", l2)
test = 0
if len(l1) == len(l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                test = 1
            else:
                test = 0
print(test)
if test == 1:
    print("Lists are same")
else:
    print("Lists are not same")
