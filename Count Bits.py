# WAP to count bits

def count_set_bits(n):
    count = 0
    while n:
        n &= n-1
        count = count + 1
    return count
n= int(input("enter n: "))
print("number of set bits:",count_set_bits(n))