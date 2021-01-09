heightValue = input("How much is height? ")
baseValue = input("How much is base? ")

if heightValue.isnumeric() and baseValue.isnumeric():
    height = int(heightValue)
    base = int(baseValue)

    area = base * height
    amountPaint = area / 2

    print("The base is {:.2f} meters and height is {:.2f} meters the area is {:.2f}m²".format(
        base, height, area))
    print("It's necessary {} paints to paint {:.2f}m²".format(
        amountPaint, area))

else:
    print("Some value isn't a number")
