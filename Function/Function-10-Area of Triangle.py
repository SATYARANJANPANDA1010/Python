#Write a program to find area of triangle

base = 0.0
height = 0.0
#here base and height are global variable

def read():
    global base,height
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))

def find_area():
    area = 0.5*base*height
    print(f'Area of triangle {area:.2f}')

def main():
    read()
    find_area()
main()
    
