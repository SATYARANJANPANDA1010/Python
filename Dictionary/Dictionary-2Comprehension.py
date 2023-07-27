# Dictionary Comprehension
# Example:3
# create dictionary with name as a key
# and 2 subject marks as value
# read the details of n students

n = int(input("Enter howmany students"))
stud={input("Enter name"):[int(input("Enter Marks")) for j in range(2)] for i in range(n)}
print(stud)

    
