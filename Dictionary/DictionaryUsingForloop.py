#for loop iterate or read key's from dictionary
#using these key's programmer can read values

marks = {101:[50,60,70],
         102:[70,80,90],
         103:[80,90,95]}
for roll in marks:
    print(roll) #print key's

#print key's with values
for roll in marks:
    print(roll,marks[roll])

#print key's with values and sum of the values
for roll in marks:
    print(roll,marks[roll],sum(marks[roll]))

#find average of each roll no
for roll in marks:
    print(roll,marks[roll],sum(marks[roll]),round(sum(marks[roll])/3,2))

mail = {'satya':'srpcode10@gmail.com',
        'ramesh':'ramesh10@gmail.com',
        'naresh':'naresh300@gmail.com'}
#print key's 
for name in mail:
        print(name)
#print key's with values
for name in mail:
    print(name,mail[name])


