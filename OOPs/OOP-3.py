class Person:
    def display(self):   #object level method
        print(f"{self}")  # "self" is having address of the obejct


def main():
    p1 = Person()
    p1.display()   # display() show the address/reference of the  p1 object
    p2 = Person()
    p2.display()   # display() show the address/reference of the  p2 object

    print(p1)      # printing the address/reference of the  p1 object
    print(p2)      # printing the address/reference of the  p2 object
main()
