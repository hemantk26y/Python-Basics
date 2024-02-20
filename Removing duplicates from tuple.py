# WAP to remove duplicate from tuple

t1 = (2, 45, 43, 45, 67, 2, 3, 8, 8, 9)
re = tuple(set(t1))
print("original tuple :", t1)
print("After removing duplicates :", re)
