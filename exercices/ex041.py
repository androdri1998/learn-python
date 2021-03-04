from datetime import datetime

birth_year = int(input("Whta's your birth year? "))

current_date = datetime.today().strftime('%Y-%m-%d')
current_year = int(current_date.split('-')[0])

current_age = current_year - birth_year

print()
print("- " * 50)
print()

if ( current_age <= 9 ):
    print("This athlete are {} years old then is a MIRIM".format(current_age))
elif ( current_age <= 14 ):
    print("This athlete are {} years old then is a INFANTIL".format(current_age))
elif ( current_age <= 19 ):
    print("This athlete are {} years old then is a JUNIOR".format(current_age))
elif ( current_age <= 25 ):
    print("This athlete are {} years old then is a SÊNIOR".format(current_age))
else:
    print("This athlete are {} years old then is a MASTER".format(current_age))

    


