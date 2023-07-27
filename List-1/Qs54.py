# GFG - Important
# Python | Sum of number digits in List

test_list = [12, 67, 98, 34]

print(f"The original list is : {test_list}")

res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum = sum + int(digit)
    res.append(sum)
print(f"List Integer Summation : {res}")





