try:
    first_number = int(input("Type first number: "))
    second_number = int(input("Type second number: "))
    third_number = int(input("Type third number: "))

    numbers = [first_number, second_number, third_number]

    higher_number = None
    for number in numbers:
        higher_number = number if higher_number == None or higher_number < number else higher_number
    
    print('The higher number is {}'.format(higher_number))
except ValueError:
    print("Some value isn't a number")