numberTyped = input("What's number to make multiplication table? ")

if numberTyped.isnumeric():
    number = int(numberTyped)
    print()
    print("Multiplication table of {}".format(number))
    for numberForMultiplication in list(range(10)):
        numberForMultiplicationIncremented = numberForMultiplication + 1
        result = number * numberForMultiplicationIncremented
        print('{} x {} = {}'.format(
            number, numberForMultiplicationIncremented, result))
else:
    print("It isn't a number")
