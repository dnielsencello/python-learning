# David Nielsen
# CS1400 - I01
# Assignment 2 task 3

# Calculating the area of a regular polygon

# Math import statement
import math
from math import pi
# Equation to calculate the sides of a polygon
# PI is imported from math module
PI = pi
# User indicates number of sides = n
n = eval(input('Input number of sides: '))
# User indicates length of sides =  s
s = eval(input('Input the length of each side: '))

# Calculation of the area of the regular polygon
area = n*math.pow(s, 2)/(4*math.tan(PI/n))

# print statement
print('The area of the regular polygon is: ' + str(round(area, 5)))
