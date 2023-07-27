# Nested loop
# WAP generating tables from 1 to 10
for num in range(1,11):
    for i in range(1,11):
        pr = num*i
        print(f'{num}*{i}={pr}')