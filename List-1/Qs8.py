# write a program to print count of even and odd numbers exist within list
list1 = [1, 5, 9, 3, 5, 7, 2, 3, 11, 15, 17, 23, 47, 22, 15, 32, 54, 76]

# using walrus operator
ec = 0
oc = 0

for value in list1:
    (ec:=ec+1) if value%2==0 else (oc:=oc+1)
print(f'List is {list1}')
print(f'Even number count {ec} ')
print(f'Odd number count {oc}')

#Another method
even_count = 0
odd_count = 0
for value in list1:
    if value % 2 == 0:
        even_count = even_count+1
    else:
        odd_count = odd_count+1
print(f'List is {list1}')
print(f'Even number count {even_count}')
print(f'Odd number count {odd_count}')