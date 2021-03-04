from datetime import datetime

birth_year = int(input("What's your birth year? "))

current_date = datetime.today().strftime('%Y-%m-%d')
current_year = int(current_date.split('-')[0])

current_age = current_year - birth_year
right_age_to_enlist = 18

if (current_year < birth_year):
    print("You aren't born yet!")
    
elif ( current_age > right_age_to_enlist ):
    years_passed = current_age - right_age_to_enlist
    year_to_enlist = current_year - years_passed
    print("You should to go enlist!")
    print("it's been {:.0f} years. should have enlisted in {}!".format(years_passed, year_to_enlist))

elif ( current_age < right_age_to_enlist ):
    years_to_go_enlist = right_age_to_enlist - current_age
    year_to_enlist = current_year + years_to_go_enlist
    print("You must enlist in {:.0f} years at {}!".format(years_to_go_enlist, year_to_enlist))

else:
    years_passed = current_age - right_age_to_enlist
    print("You must to go enlist! it's right age.")

