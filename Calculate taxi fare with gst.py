# WAP to calculate fare of  a taxi based on desired taxi and distance with gst


def Cab_Fare(des, km):
    if des == 1 or des == 2:
        fare = 13 * km
        f_gst = fare*0.05
        t_fare = fare+f_gst
        print("Your Fare is", fare)
        print("Your Total Fare(Including GST) is", t_fare)
    elif des == 3:
        fare = 19 * km
        f_gst = fare * 0.05
        t_fare = fare + f_gst
        print("Your Fare is", fare)
        print("Your Total Fare(Including GST) is", t_fare)
    elif des == 4:
        fare = 12 * km
        f_gst = fare * 0.05
        t_fare = fare + f_gst
        print("Your Fare is", fare)
        print("Your Total Fare(Including GST) is", t_fare)
    elif des == 5:
        fare = 25 * km
        f_gst = fare * 0.05
        t_fare = fare + f_gst
        print("Your Fare is", fare)
        print("Your Total Fare(Including GST) is", t_fare)
    else:
        print("Entered wrong input")


print("Prime Sedan : 1, Prime Play : 2, Prime SUV : 3, Mini : 4, Lux : 5")
des1 = int(input("select your desired cab :"))
km1 = int(input("enter the Kilo meters you want ride :"))
Cab_Fare(des1, km1)
