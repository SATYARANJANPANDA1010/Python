#Python Program for Program to find area of a circle
radius = int(input("Enter radius: "))
area = 3.14 * radius * radius
print(f"Area of circle is {area}")


#another method using Math module
import math
area1 = math.pi * radius * radius
print(f"Area of circle is {round(area,2)}")
