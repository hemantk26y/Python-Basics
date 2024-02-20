# WAP to check key exist in dictionary or not

d1 = {"Name": "Hemant", "Age": 20, "City": "New Delhi"}
k = input("Enter the key to search : ")
if k in d1.keys():
    print(k, "Value found in the Dictionary")
else:
    print(k, "Value not exist in the Dictionary")

