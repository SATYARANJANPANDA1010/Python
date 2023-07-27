# GFG
# 2nd method
# Python – Remove empty List from List

test_list = [5, 6, [], 3, [], [], 9]

print(f'Original Test_list {test_list}')

while [] in test_list:
    test_list.remove([])
print(f'New test list is {test_list}')
