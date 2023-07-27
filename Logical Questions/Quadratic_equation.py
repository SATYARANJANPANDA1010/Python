'''

'''
import cmath
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = float(input("Enter a number: "))
s = (b**2)-(4*a*c)
f1 = (-b+ cmath.sqrt(s))/(2*a)
f2 = (-b- cmath.sqrt(s))/(2*a)
print(f'The solution is {f1} and {f2}')
