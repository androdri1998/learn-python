from datetime import date

try:
    year = int(input("Type a year or type 0 to get current year: "))

    if year == 0:
        year = date.today().year

    is_leap_year = False
    rest_by_4 = year % 4
    rest_by_100 = year % 100
    rest_by_400 = year % 400

    if(rest_by_4 == 0 and rest_by_100 != 0 or rest_by_400 == 0):
        is_leap_year = True
    
    print('{} is a leap year'.format(year) if is_leap_year else "{} isn't a leap year".format(year))
    
except ValueError:
    print("Value isn't a number")