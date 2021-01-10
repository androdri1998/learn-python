number_typed = input("What's number to make multiplication table? ")

try:
    number = int(number_typed)
    print()
    print("Multiplication table of {}".format(number))
    for number_for_multiplication in list(range(10)):
        number_for_multiplication_incremented = number_for_multiplication + 1
        result = number * number_for_multiplication_incremented
        print('{} x {} = {}'.format(
            number, number_for_multiplication_incremented, result))
except ValueError:
    print("It isn't a number")
