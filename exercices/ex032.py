try:
    year = int(input("Type a year? "))

    is_leap_year = False
    rest_by_4 = year % 4
    rest_by_100 = year % 100
    rest_by_400 = year % 400

    if(rest_by_4 == 0 or rest_by_100 == 0 or rest_by_400 == 0):
        is_leap_year = True
    
    print('Is a leap year' if is_leap_year else 'Is not a leap year')
    
except ValueError:
    print("Value isn't a number")