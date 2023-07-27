# Example:1
# WAP to create dictionary with number and number power 2
# {1:1,2:4,3:9,4:16,5:25...n:n pow 2}
dict1 = {}
n = int(input("Enter number"))
for i in range(1,n+1):
    dict1[i] = i**2
print(dict1)

# Example:2
# create ascii chart dictionary
# {key:value,key:value,....}
# {'A':65,'B':66,'C':67,...}

dict2 = {}
for num in range(65,91):
    dict2[chr(num)] = num
print(dict2)





    
    
