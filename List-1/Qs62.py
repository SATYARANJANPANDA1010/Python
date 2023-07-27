# GFG
# 1st method
# Python – Remove empty List from List

test_list = [5, 6, [], 3, [], [], 9]
print(f'Test the original list {test_list}')
new_list = []
for ele in test_list:
    if ele:
        new_list.append(ele)
print(f'New List is: {new_list}')
