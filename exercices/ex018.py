from math import radians, sin, cos, tan

degree_value = input("Type a degree: ")

try:
    degree = float(degree_value)
    degree_in_radians = radians(degree)
    sine = sin(degree_in_radians)
    cosine = cos(degree_in_radians)
    tangent = tan(degree_in_radians)
    print('The sine is {:.2f}'.format(sine))
    print('The cosine is {:.2f}'.format(cosine))
    print('The tangent is {:.2f}'.format(tangent))
    
except ValueError:
    print("Value isn't a number")