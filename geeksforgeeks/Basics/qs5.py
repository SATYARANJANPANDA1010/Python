#Python Program for Program to find the sum of a Series 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!

num = int(input("Enter a number: "))
sum = 0
fact= 1
for i in range(1,num+1):
    fact = fact*i
    sum = sum+(i/fact)
print(sum)

