#takes a user input number and finds whether it is even or odd.
#If the number is odd, then it finds the multiple of 10 number that comes after the input number:
num = int(input("Enter a number: "))
if num%2 == 0:
    print(f"{num}It's a even number")
else:
    print(f'{num} is a odd number ')
    print("The next multiple of 10 after",num,"is",((num//10)+1)*10)
