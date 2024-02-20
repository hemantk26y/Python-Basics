# WAP to sort a set

s1 = {3, 4, 6, 10, 2, 1}
s1 = list(s1)
for i in range(len(s1)):
    for j in range(i + 1, len(s1)):
        if s1[i] > s1[j]:
            s1[i], s1[j] = s1[j], s1[i]
print(set(s1))
