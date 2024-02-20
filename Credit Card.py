# WAP to check validity of credit card

cc_no = 4111111111111178
temp = str(cc_no)

sum1 = 0
sum2 = 0

index = len(temp) - 1
while index >= 0:
    sum1 = sum1 + int(temp[index])
    index = index - 2

index = len(temp) - 2
while index >= 0:
    n = int(temp[index]) * 2
    if n >= 10:
        n = str(n)
        sum2 = sum2 + int(n[0]) + int(n[1])
    else:
        sum2 = sum2 + n
    index = index - 2

total = str(sum1 + sum2)
valid_val = int(total[len(total) - 1])

if valid_val == 0:
    print("valid")
else:
    print("invalid")