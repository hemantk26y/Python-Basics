# WAP to checksum

def checksum(credit):
    st = str(credit)
    s_o = 0
    s_e = 0

    for i in range(len(st)):
        if (i == 0) or (i % 2 == 0):
            num = str(i * 2)
            if num == 2:
                s_o += int(st[i])
        else:
            s_e += int(st[i])
    s_t = s_o + s_e
    if s_t % 10 == 0:
        print("Valid Credit Card Number")
    else:
        print("Not Valid Credit Card Number")


n = int(input("Enter the Credit Card Number : "))
checksum(n)
