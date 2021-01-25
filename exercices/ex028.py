from random import randint
from time import sleep

drawed_number = randint(0, 5)

print('-=-' * 20)
print("I'll think in a number between 0 and 5... try to guess")
print('-=-' * 20)

try:
    hunch = int(input("What's your guess? "))
    print("I'm Thinking...")
    sleep(3)
    print("you're right" if hunch == drawed_number else 'you missed, i think in {}'.format(drawed_number))
    
except ValueError:
    print("Value isn't a number")