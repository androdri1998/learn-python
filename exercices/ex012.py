price_value = input("How many does the product cost? R$ ")

try:
    price = float(price_value)
    discount = price * 0.05
    new_price = price - discount
    print("The product costs R$ {:.2f} and with a 5% discount costs R$ {:.2f}.".format(
        price, new_price))
except ValueError:
    print("It isn't a number")
