try:
    number = int(input("Type a number: "))
    
    rest = number % 2
    print('{} is even'.format(number) if rest == 0 else '{} is odd'.format(number))
    
except ValueError:
    print("Value isn't a number")