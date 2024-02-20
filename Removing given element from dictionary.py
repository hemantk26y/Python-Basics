# WAP to remove given element from the dictionary

dict1 = {'a': 100, 'b': 200, 'c': 300}
print('original dictionary: ', dict1)
k = input('enter the key you want to remove: ')
if k in dict1.keys():
    dict1.pop(k)
print('new dict: ', dict1)
