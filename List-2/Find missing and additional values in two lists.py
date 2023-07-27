list1=[1,2,3,4,5,6]
list2=[4,5,6,7,8]
A=set(list1)
B=set(list2)
print(f'List1 Values {list1}')
print(f'List2 Values {list2}')
print(f'Missing Values in List1 {B-A}')
print(f'Additional Values in List2 {A-B}')
print(f'Missing Values in List2 {A-B}')
print(f'Additional Values in List2 {B-A}')

    
