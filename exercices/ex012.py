priceValue = input("How many does the product cost? ")

if priceValue.isnumeric():
    price = int(priceValue)
    discount = price * 0.05
    newPrice = price - discount
    print("The product costs R$ {:.2f} and with a 5% discount costs R$ {:.2f}.".format(
        price, newPrice))
else:
    print("It isn't a number")
