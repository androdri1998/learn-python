incomeValue = input("How much is the income? ")

if incomeValue.isnumeric():
    income = int(incomeValue)
    incrementIncome = income * 0.15
    newIncome = income + incrementIncome
    print("Your current income is R$ {:.2f} and with a 15% increment will to be R$ {:.2f}.".format(
        income, newIncome))
else:
    print("It isn't a number")
