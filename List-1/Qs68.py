# STACK
# WAP of STACK operation
stack = []
while True:
    print("***MENU***")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    opt = int(input("Enter your option: "))
    if opt == 1:
        ele = int(input("Enter elements: "))
        stack.append(ele)
        print("element pushed inside stack")
    elif opt == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            ele = stack.pop()
            print(f"{ele} poped from stack")
    elif opt == 3:
        print(f'Stack: {stack}')
    elif opt == 4:
        break

