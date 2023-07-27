class Course:
    def create_properties(self):
        self.cname = None
        self.fees = None

def main():
    course1 = Course()
    course1.create_properties()
    course2 = Course()
    course2.create_properties()
    print(course1.cname,course1.fees)
    print(course2.cname,course2.fees)
main()