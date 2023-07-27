# Function with optional arguments  or default arguments


# Calculate simple_interest --> default rate of interest arguments

def simple_interest(p,t):
    si = (p*t*1.5)/100
    return si

#old function replaced by new function,because in python function overloading not supported
def simple_interest(p,t,r=1.5):
    si = p*t*r/100
    return si

res1 = simple_interest(6000,12)
res2 = simple_interest(4000,25)
res3 = simple_interest(5000,23,3.5)  #default argument of r=1.5 replace by r=3.5
print(res1,res2,res3)

