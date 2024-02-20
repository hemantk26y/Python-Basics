# ========== Simple Interest =========

p = float(input("Principle amount : "))
r = float(input("Rate of interest : "))
t = int(input("Time period(in years) : "))
simple_interest = (p*r*t)/100
amount = p+simple_interest
print("Simple Interest :", simple_interest)
print("Total Amount with SI", amount)
