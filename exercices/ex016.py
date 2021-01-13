from math import trunc

decimal_number_value = input("Type a decimal number: ")

try:
    decimal_number = float(decimal_number_value)
    number_int = trunc(decimal_number)
    print('The integer part is {}'.format(number_int))
except ValueError:
    print("Value isn't a number")