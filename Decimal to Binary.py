# WAP to convert decimal to binary number

def Countbits(dec):
    dec1 = dec
    s = ""
    c_bits = 0
    while dec1 > 0:
        bn = dec1 % 2
        s += str(bn)
        dec1 = dec1 // 2
    s1 = s[::-1]
    for i in range(len(s)):
        c_bits += int(s[i])
    print("Decimal(Original Number) :", dec)
    print("Binary(after conversion into binary) :", s1)
    print("Number of Bits in ", s1, "is", c_bits)


d = int(input("Enter the number :"))
Countbits(d)
