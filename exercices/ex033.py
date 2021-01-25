try:
    first_number = int(input("Type first number: "))
    second_number = int(input("Type second number: "))
    third_number = int(input("Type third number: "))

    numbers = [first_number, second_number, third_number]

    higher_number = first_number
    smaller_number = first_number
    for number in numbers:
        smaller_number = number if smaller_number > number else smaller_number
        higher_number = number if higher_number < number else higher_number
    
    print('The higher number is {} and smaller number is {}'.format(higher_number, smaller_number))
except ValueError:
    print("Some value isn't a number")