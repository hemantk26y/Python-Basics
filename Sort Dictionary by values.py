# WAP to sort a dictionary by values


d1 = {'a': 20, 'b': 4000, 'c': 900, 'd': 100}
itm = list(d1.items())
for i in range(len(itm) - 1):
    for j in range(i + 1, len(itm)):
        if itm[i][1] > itm[j][1]:
            t = itm[i]
            itm[i] = itm[j]
            itm[j] = t
sortdict = dict(itm)
print("Original dictionary : ", d1)
print("Sorted dictionary : ", sortdict)
