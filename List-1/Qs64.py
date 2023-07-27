# GFG - Important
# Qs --> 54
# In another way
# Python | Sum of number digits in List

test_list = [12, 67, 98, 34]
new_list = []
for num in test_list:
    add = 0
    while num > 0:
        var = num%10
        add = add+var
        num = num//10
    new_list.append(add)

print(f'Sum of number digit in the list is {new_list}')