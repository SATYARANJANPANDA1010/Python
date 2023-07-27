#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

n1 = input("Enter the first name: ")
n2 = input("Enter the last name: ")
print(n2+" "+n1)



# Another method
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
# Combine first and last names into a list
name_list = [first_name,last_name]
## Reverse the order of the list using the reverse() method
name_list.reverse()
# join() method to combine the list elements into a single string separated by a space
reverse_name = " ".join(name_list)
print(reverse_name)