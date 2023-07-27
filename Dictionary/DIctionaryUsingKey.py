#Using Key
course = {"java":2000,
          "python":4000,
          "webdev":8000}
print(course)
print(course["java"]) #we can read value from dictionary using key
print(course["python"])
#if the key doesnot exist with in dictionary then it will display key error

#print(course["oracle"])
#output-KeyError: 'oracle'

sales= {2018:40000,
        2019:50000,
        2020:60000,
        2021:70000,
        2022:80000}
print(sales[2020])
