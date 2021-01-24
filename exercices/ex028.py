from random import randint

drawed_number = randint(1, 5)

try:
    hunch = int(input("What's your guess? "))
    print("you're right" if hunch == drawed_number else 'you missed')
    
except ValueError:
    print("Value isn't a number")