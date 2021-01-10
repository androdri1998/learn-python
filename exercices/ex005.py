input_value = input('Type a number: ')

try:
    int_value = int(input_value)
    previous_number = int_value - 1
    next_number = int_value + 1
    print("The number entered is {} and its previous number is {} and the next number is {}".format(
        int_value, previous_number, next_number))
except ValueError:
    print("It isn't a number")
