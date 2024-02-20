# WAP to map list to dictionary

# Keys = [‘a’,’b’,’c’,’d’]
# Values = [1,2,3,4]
# map two lists into a dictionary
keys = ['Blue', 'Green', 'Red']
values = [200, 300, 400]
color = dict(zip(keys, values))
print('keys list = ', keys)
print('values list = ', values)
print('mapped dictinary = ', color)
