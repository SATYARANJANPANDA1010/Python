accounts = {101:['naresh',50000],
            102:['suresh',65000],
            103:['ramesh',25000]}
accno = int(input("Enter Account Number: "))
if accno in accounts:
    Transaction_type = input("Transaction Type(D/W): ")
    Transaction_amount = int(input("Transaction Amount: "))
    if Transaction_type == 'D' or Transaction_type == 'd':
        accounts[accno][1] = accounts[accno][1]+Transaction_amount
    elif Transaction_type == 'W' or Transaction_type == 'w':
        if Transaction_amount>accounts[accno][1]:
            print("Insufficient Balance")
        else:
            accounts[accno][1] = accounts[accno][1] - Transaction_amount
    print(accno,accounts[accno])
else:
    print(f'{accno} invalid')
