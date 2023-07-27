n1=int(input("Enter First Number"))
n2=int(input("Enter Second Number"))
def add():
    print(f'sum is {n1+n2}')
def sub():
    print(f'diff is {n1-n2}')
def multiply():
    print(f'product is {n1*n2}')
def div():
    print(f'result is {n1/n2:.2f}')

def main():
    opr=input("Enter Operator")
    if opr == '+':
        add()
    elif opr == '-':
        sub()
    elif opr == '*':
        multiply()
    elif opr == '/':
        div()
    else:
        print("Invalid operator")
main()   
