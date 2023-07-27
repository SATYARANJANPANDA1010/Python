#Questions-HRA


#HRA is lowest of below value.
#1)Actual HRA received from employer
#2)For those living in metro cities: 50% of (Basic salary + Dearness allowance)
#For those living in non-metro cities: 40% of (Basic salary + Dearness allowance)
#3)Actual rent paid minus 10% of (Basic salary + Dearness allowance)


#Write a python program which takes input and output the HRA exemption.



def hra_exemption(basic, da, city, hra, rent):
    if city == "metro":
        hra1 = 0.5 * (basic + da)
    else:
        hra1 = 0.4 * (basic + da)
    hra2 = rent - 0.1 * (basic + da)
    hra3 = hra
    return min(hra1, hra2, hra3)

basic = float(input("Enter basic salary: "))
da = float(input("Enter dearness allowance: "))
city = input("Enter city (metro/non-metro): ")
hra = float(input("Enter actual HRA received: "))
rent = float(input("Enter actual rent paid: "))

print("HRA exemption:", hra_exemption(basic, da, city, hra, rent))
