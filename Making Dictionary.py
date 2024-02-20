# WAP to make a dictionary with values

my_dict = {}
n = int(input('enter the number of elements in the dictionary: '))
for i in range(1, n + 1):
    my_dict[i] = i * i
print("Dictionary with element (x*x) -->", my_dict)
