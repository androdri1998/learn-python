input_value = input('Type a number: ')

try:
    int_value = int(input_value)
    double_value = int_value * 2
    triple_value = int_value * 3
    square_root_value = int_value ** (1/2)

    print("The number entered is {:.2f} and its double is {:.2f} and its triple is {:.2f} and its square root is {:.2f}".format(
        int_value, double_value, triple_value, square_root_value))

except ValueError:
    print("It isn't a number")
