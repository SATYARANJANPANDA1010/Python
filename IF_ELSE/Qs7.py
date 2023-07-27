# Application to find area
dim1 = float(input("Enter Dim1: "))
dim2 = float(input("Enter Dim2: "))
print("1.Triangle")
print("2.Rectangle")
opt = int(input("Enter Option: "))
match(opt):
    case 1:
        print(f'Area of Triangle is: {0.5*dim1*dim2}')
    case 2:
        print(f'Area of Rectangle is: {dim1*dim2}')
    case _:
        print("invalid input try again")