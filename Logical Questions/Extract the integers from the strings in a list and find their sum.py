# Define the list of strings
strings = ["Satya10", "Naresh20", "Smruti30", "Hari34", "Sounmy76"]

int_sum = 0

for string in strings:
    digit = ""
    for char in string:

        if char.isdigit():
            digit = digit+char
    int_sum = int_sum+int(digit)

print(f'The sum of integers in the list is:{int_sum}')
