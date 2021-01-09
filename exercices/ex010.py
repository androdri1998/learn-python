moneyValue = input("How many money do you have? ")

if moneyValue.isnumeric():
    money = int(moneyValue)
    dollars = money / 5.42
    print()
    print("You have R$ {:.2f} reais equal to $ {:.2f} dollars".format(
        money, dollars))

else:
    print("It isn't a number")
