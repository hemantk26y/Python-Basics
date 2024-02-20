# WAP to swap position in dictionary

my_dict = {'A': 100, 'B': 400, 'C': 500}
my_list = list(my_dict.items())
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        my_list[i], my_list[j] = my_list[j], my_list[i]
        break
print('original dictionary = ', my_dict)
print('swapped items dictionary = ', dict(my_list))
