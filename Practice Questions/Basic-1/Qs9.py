#Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
string = " "
for d in exam_st_date:
    string = string+str(d)

# Extract the date from the tuple
exam_date = "/".join(str(d) for d in exam_st_date)

# Print the examination schedule
print("The examination will start from:", exam_date)

