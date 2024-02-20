""">=20,000 (20% of total bill)
>=15,000 (10% of total bill)
>=10,000 (5% of total bill)
Otherwise NO DISCOUNT
Write a program to input the total bill value from the user and then calculate the discount amount, total bill after
discount and the discounted %.
"""
bill = int(input("Amount : "))

if bill >= 20000:
    dis = bill*0.20
    t_bill = bill - dis
    print("Your Bill (before discount) :", bill)
    print("Discount you own :", dis)
    print("Your Net Bill (after discount) :", t_bill)
elif bill >= 15000:
    dis = bill*0.10
    t_bill = bill - dis
    print("Your Bill :", bill)
    print("Discount you own :", dis)
    print("Your Net Bill (after discount) :", t_bill)
elif bill >= 10000:
    dis = bill*0.05
    t_bill = bill - dis
    print("Your Bill :", bill)
    print("Discount you own :", dis)
    print("Your Net Bill (after discount) :", t_bill)
else:
    dis = 0
    t_bill = bill
    print("Your Bill :", bill)
    print("Discount you own :", dis)
    print("Your Net Bill (after discount) :", t_bill)
