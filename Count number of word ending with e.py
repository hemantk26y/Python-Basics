# WAP to count of words ending with 'e'

with open("dummyfile1.txt") as f:
    a = f.read()
    words = a.split()
    c = 0
    for i in words:
        if i[-1]=='e':
            c += 1
    print(c)