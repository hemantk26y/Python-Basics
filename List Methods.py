# WAP to use list methods

l1 = ["Rohit", "K L Rahul", "Virat", "SKY", "R Pant", "D Kartik"]
l2 = ["Hardik", "R Jadeja", "Bhuvi", "Y Chahel", "J Bumrah"]
l1.append("D Hooda")
print("Append l2 to l1 -->", l1)
l3 = []
l3.clear()
print("Clear -->", l3)
print("Copy -->", l2.copy())
print("Count -->", l1.count("r"))
l3.extend(l2)
print("Extend l3 to l2 -->", l3)
print("Index Number of 'Bhuvi' -->", l2.index("Bhuvi"))
print("Insert 'A Patel' -->", l1.insert(2, "A Patel"))
print("Pop -->", l3.pop())
try:
    l3.remove("R jadeja")
except ValueError:
    print("Remove 'D Kartik' -->", l3)
l2.reverse()
print("Reverse -->", l2)
l1.sort()
print("Sort l1 -->", l1)
