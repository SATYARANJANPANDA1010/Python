n = int(input("Enter the number of calls: "))
ruppees = 200
if n>0 and n<=100:
    print(f"Minimum bill Rs.-->{ruppees}")
elif n>100 and n<=150:
    print(f'Minimum bill Rs.--> {ruppees+(n-100)*0.60}')
elif n>150 and n<=200:
    print(f'Minimum bill Rs. --> {ruppees+50*0.60+(n-150)*0.50}')
else:
    print(f'Minimum bill Rs. --> {ruppees+50*0.60+50*0.50+(n-200)*0.40}')



