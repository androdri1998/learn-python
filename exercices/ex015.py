days_value = input("How many days did you rent the car? ")
kilometers_value = input("How many kilometers did you drive? ")

try:
    days = int(days_value)
    kilometers = float(kilometers_value)

    price_day_rent_car = 60
    price_car = days * price_day_rent_car

    price_per_kilometer_drived = 0.15
    price_kilometers_drived = kilometers * price_per_kilometer_drived

    price_rent = price_car + price_kilometers_drived

    print("The car rental costed R$ {:.2f}".format(price_rent))

except ValueError:
    print("Some value isn't a number")
