house_price = float(input("How much is this house? R$ "))
income = float(input("How much is your income? R$ "))
year_to_pay = int(input("How many years will you pay? "))

amount_months = 12
total_amount_months_to_pay = year_to_pay * amount_months

percentage_limit_allowed_to_pay_with_income = 0.3
amount_allowed_to_pay_with_month = income * percentage_limit_allowed_to_pay_with_income

installment_value = house_price / total_amount_months_to_pay

is_eligible_for_loan = False
if( installment_value <= amount_allowed_to_pay_with_month):
    is_eligible_for_loan = True

print()
print("- " * 50)
print()

print("You income is R$ {:.2f}!".format(income))
print("Your max installment value allowed per month is R$ {:.2f}!".format(amount_allowed_to_pay_with_month))
print("Installment value per month required is R$ {:.2f}!".format(installment_value))
print("You are eligible for the loan!" if is_eligible_for_loan else "You aren't eligible for the loan!")