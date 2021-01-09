inputValue = input('Type a number: ')

if inputValue.isnumeric():
    intValue = int(inputValue)
    previousNumber = intValue - 1
    nextNumber = intValue + 1
    print("The number entered is {} and its previous number is {} and the next number is {}".format(
        intValue, previousNumber, nextNumber))
else:
    print("It isn't a number")
