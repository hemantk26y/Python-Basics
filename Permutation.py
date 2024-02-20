# WAP to perform permutation

initial_val = str(input('enter the number or characters; '))
result = []
print('Initial value', initial_val)
def permutation(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permutation(data, i + 1, length)
            data[i], data[j] = data[j], data[i]
permutation(list(initial_val), 0, len(initial_val))
print('the resultant permutations are: ', result)
