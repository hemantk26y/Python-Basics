# WAP to sort a dictionary by keys

dict1 = {'m': 786, 'b': 111, 'n': 777, 'd': 108}
items = list(dict1.items())
for i in range(len(items) - 1):
    for j in range(i + 1, len(items)):
        if items[i][0] > items[j][0]:
            t = items[i]
            items[i] = items[j]
            items[j] = t
sortdict = dict(items)
print('original dictionary = ', dict1)
print('sorted dict = ', sortdict)
