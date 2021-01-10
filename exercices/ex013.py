income_value = input("How much is the income? R$ ")

try:
    income = float(income_value)
    increment_income = income * 0.15
    new_income = income + increment_income
    print("Your current income is R$ {:.2f} and with a 15% increment will to be R$ {:.2f}.".format(
        income, new_income))
except ValueError:
    print("It isn't a number")
