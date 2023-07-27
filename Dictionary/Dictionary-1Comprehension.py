#Dictionary Comprehension
#Comprehension is another method or approach of creating collections like:list,set and dictionary
#comprehension allpws creating dictionary in easy approach

#syntax1: {key:value for variable in iterable}

#Example: WAP to create dictionary with number and number power 2
#{1:1,2:4,3:9,4:16,5:25...n:n pow 2}

n = int(input("Enter the number"))
dict1 = {num:num**2 for num in range(1,n+1)}
print(dict1)
