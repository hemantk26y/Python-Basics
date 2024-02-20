""" WAP to calculate total salary of the person and tax is 15% which is to be deducted """

b_s = int(input("enter the salary :"))
hra = b_s*(27/100)
da = b_s*(28/100)
tax = b_s*(15/100)
a_s = (b_s+hra+da) - tax
print(a_s)
