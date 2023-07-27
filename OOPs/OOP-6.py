class Student:
    def __init__(self):
        #instance variable
        self.rollno = None
        self.name = None
        self.course = None
def main():
    student1 = Student()
    student2 = Student()
    comp1 = complex() #pre-defined data type
    print(student1.name,student1.course,student1.rollno)
    print(student2.name,student2.course,student2.rollno)
    print(comp1.real,comp1.imag)  # .real & .imag are variables of complex

main()