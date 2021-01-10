meters_value = input('How many meters do you want to convert? ')

try:
    meters = float(meters_value)
    kilometers = meters / 1000
    hectometers = meters / 100
    decameters = meters / 10
    decimeters = meters * 10
    centimeters = meters * 100
    millimeters = meters * 1000

    print("{:.2f} meters equal to: ".format(
        meters))
    print("{:.3f}km".format(
        kilometers))
    print("{:.3f}hm".format(
        hectometers))
    print("{:.3f}dam".format(
        decameters))
    print("{:.0f}dm".format(
        decimeters))
    print("{:.0f}cm".format(
        centimeters))
    print("{:.0f}mm".format(
        millimeters))
except ValueError:
    print("It isn't a number")
