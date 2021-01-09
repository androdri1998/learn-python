inputValue = input('Type a number: ')

if inputValue.isnumeric():
    intValue = int(inputValue)
    doubleValue = intValue * 2
    tripleValue = intValue * 3
    squareRootValue = intValue ** (1/2)

    print("The number entered is {} and its double is {} and its triple is {} and its square root is {:.2f}".format(
        intValue, doubleValue, tripleValue, squareRootValue))

else:
    print("It isn't a number")
