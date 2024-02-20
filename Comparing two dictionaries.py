# WAP to compare two dictionaries


dict1 = {'a': 100, 'B': 200, 'c': 300}
dict2 = {'a': 100, 'B': 200, 'c': 300}
x = ''
if len(list(dict1.items())) == len(list(dict2.items())):
    l1 = len(list(dict1.items()))
    for i in range(l1):
        if list(dict1.items())[i] == list(dict2.items())[i]:
            x = 'dict1 and dict2 are identical.'
        else:
            x = 'dict1 and dict2 are not identical.'
else:
    x = 'dict1 and dicT2 are not of the same length.'

print('dictionary 1 = ', dict1)
print('dictionary 2 = ', dict2)
print(x)
