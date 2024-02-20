# WAP to combine two dictionaries


dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 200, 'b': 450, 'c': 550}
sum_values = [sum(i) for i in zip(dict1.values(), dict2.values())]
new_dict = dict(zip(dict1.keys(), sum_values))
print('dictionary 1 = ', dict1)
print('dictionary 2 = ', dict2)
print('combined dictionary = ', new_dict)
