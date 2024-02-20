# WAP to remove intersection of 2nd set

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
print("First set: ", set1)
print("Second set: ", set2)
int_sec = set2.intersection(set1)
print("Intersection of the set: ", int_sec)
set3 = set1.difference(int_sec)
print("After removing intersection from set1: ", set3)
