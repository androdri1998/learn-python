metersValue = input('How many meters do you want to convert? ')

if metersValue.isnumeric():
    meters = int(metersValue)
    centimeters = meters * 100
    millimeters = meters * 1000

    print("{} meters contain {} centimeters and also can contain {} millimeters".format(
        meters, centimeters, millimeters))
else:
    print("It isn't a number")
