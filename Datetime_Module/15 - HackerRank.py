import datetime

# number of test cases
t = int(input())
for i in range(t):
    # read two time stamps
    t1 = datetime.datetime.strptime(input().strip(), "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.datetime.strptime(input().strip(), "%a %d %b %Y %H:%M:%S %z" )

    # calculate the absolute difference in seconds
    diff = abs(int((t1-t2).total_seconds()))

    # Output
    print(diff)