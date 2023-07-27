#Pattern-8

'''
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
'''

#if row is odd print 1
#if row is even print 0

for r in range(1,6):
    for c in range(1,6):
        if r%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
