height_value = input("How much is height? ")
base_value = input("How much is base? ")

try:
    height = int(height_value)
    base = int(base_value)

    area = base * height
    amount_paint = area / 2

    print("The base is {:.2f} meters and height is {:.2f} meters the area is {:.2f}m²".format(
        base, height, area))
    print("It's necessary {} paints to paint {:.2f}m²".format(
        amount_paint, area))

except ValueError:
    print("Some value isn't a number")
