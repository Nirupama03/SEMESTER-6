#write a numpy pgm to capitalize  the first letter , lowercase , uppercase, titlecase of all the elements of the given array

import numpy as py

l=['Hi','Hello','world','Good','Morning']
x = py.array(l,dtype=str)

print("The original array is :")
print(x)

a = py.char.capitalize(x)
b = py.char.lower(x)
c = py.char.upper(x)
d = py.char.title(x)

print("Capitalized :",a)
print("Lower Case :",b)
print("Upper Case :",c)
print("Title case :",d)