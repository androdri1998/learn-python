from math import hypot

oposite_side_value = input("Type a oposite side: ")
adjacent_side_value = input("Type a adjacent side: ")

try:
    oposite_side = float(oposite_side_value)
    adjacent_side = float(adjacent_side_value)
    
    hypotenuse = hypot(adjacent_side, oposite_side)
    print('The hypotenuse is {:.2f}'.format(hypotenuse))

except ValueError:
    print("Some value isn't a number")