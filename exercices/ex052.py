number = int(input('Type a integer number: '))

found_cousin_number = False
position_founded = None
if(number > 1):
    for index in range(2, number + 1):
        if(number%index == 0):
            found_cousin_number = True
            position_founded = index
            break

if(number <= 1):
    print("{} it isn't a cousin number".format(number))
elif(position_founded == number and found_cousin_number):
    print("{} it's a cousin number".format(number))
else:
    print("{} it isn't a cousin number".format(number))
