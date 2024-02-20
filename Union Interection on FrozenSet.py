# WAP to find union, intersection and difference of two given set

set1 = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9})
set2 = frozenset({4, 6, 8, 9, 10, 12, 14, 15, 16, 18})
print("First set: ", set1)
print("Second set: ", set2)
print("Union of the set: ", set1.union(set2))
print("Intersection of the set: ", set1.intersection(set2))
print("Difference of the set: ", set1.difference(set2))
