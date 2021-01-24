try:
    income = int(input("How much is your income? R$ "))
    
    new_income = 0
    if(income > 1250):
        increment = income * 0.1
    else:
        increment = income * 0.15

    new_income = income + increment

    print('Your new income is R$ {:.2f}'.format(new_income))
except ValueError:
    print("Some value isn't a number")