money_value = input("How many money do you have? ")

try:
    money = float(money_value)
    dollars = money / 5.42
    print()
    print("You have R$ {:.2f} reais equal to $ {:.2f} dollars".format(
        money, dollars))

except ValueError:
    print("It isn't a number")
