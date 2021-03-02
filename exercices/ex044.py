price_product = float(input("How much is the product? R$ "))
print()
print(" 1 - in cash")
print(" 2 - 1x at credit card")
print(" 3 - 2x at credit card")
print(" 4 - 3x or more at credit card")
print()
payment_condition = int(input("What's payment condition? "))

print()
print("- " * 50)
print()

if ( payment_condition >= 1 and payment_condition <= 4):
    full_name_condition_payments = [
        "in cash",
        "1x at credit card",
        "2x at credit card",
        "3x or more at credit card",
    ]

    type_in_cash = 1
    type_1x_credit_card = 2
    type_2x_credit_card = 3
    type_3x_or_more_installments_credit_card = 4 

    new_price_product = 0
    if ( payment_condition == type_in_cash ):
        discount = price_product * 0.1
        new_price_product = price_product - discount
    elif ( payment_condition == type_1x_credit_card ):
        discount = price_product * 0.05
        new_price_product = price_product - discount
    elif ( payment_condition == type_2x_credit_card ):
        new_price_product = price_product
    else:
        fees = price_product * 0.2
        new_price_product = price_product + fees

    full_name_condition_payment = full_name_condition_payments[payment_condition - 1]

    print("This product with price R$ {:.2f} and condition payment {}, have as final price R$ {:.2f}".format(price_product, full_name_condition_payment, new_price_product))

else:
    print("It isn't a valid condition payment")