p = float(input("enter the amount"))
t = int(input("enter the time"))
r = float(input("enter the rate"))
si = p*t*r/100
print('''Amount:%.2f
Time:%d
Rate:%.2f
Simple interest:%.2f'''%(p,t,r,si))
