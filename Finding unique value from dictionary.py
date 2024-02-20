# WAP to find unique value in dictionary

"""
dict1 = {'a': 100, 'B': 100, 'c': 300}
unique_dict = dict()
for i in dict1.values():
    for j in dict1.values():
        if i != j:
            unique_dict[] = dict1[i]
            unique_dict[j] = dict[j]
            break
print('original dictionary = ', dict1)
print('New Dictionary = ', unique_dict)
"""
dict1 = {'a': 100, 'b': 100, 'c': 300}
val = dict1.keys()
k = dict1.values()
unique_dict = dict()
for i in dict1.keys():
    for j in dict1.keys():
        if i!=j:
            if dict1[i] != dict1[j]:
                unique_dict[i]=dict1[i]
                unique_dict[i] = dict1[i]
                break

print('original dictionary = ', dict1)
print('New Dictionary = ', unique_dict)
