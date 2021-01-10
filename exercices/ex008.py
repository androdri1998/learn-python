meters_value = input('How many meters do you want to convert? ')

try:
    meters = float(meters_value)
    centimeters = meters * 100
    millimeters = meters * 1000

    print("{:.2f} meters contain {:.0f} centimeters and also can contain {:.0f} millimeters".format(
        meters, centimeters, millimeters))
except ValueError:
    print("It isn't a number")
