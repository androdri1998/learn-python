from random import randrange

print(" 1 - Stone")
print(" 2 - Paper")
print(" 3 - Scissors")
print()
move_user = int(input("What's your move? "))

def jokenpo ( move_one, move_two ):
    draw = 0
    stone = 1
    paper = 2
    scissors = 3

    if ( move_one == move_two ):
        return draw
    elif ( move_one == stone and move_two == paper or move_two == stone and move_one == paper):
        return paper
    elif ( move_one == stone and move_two == scissors or move_two == stone and move_one == scissors):
        return stone
    elif ( move_one == paper and move_two == scissors or move_two == paper and move_one == scissors):
        return scissors

if ( move_user >= 1 and move_user <= 3 ):
    full_name_moves = [
        "stone",
        "paper",
        "scissors"
    ]

    move_machine = randrange(1,4)

    move_win = jokenpo( move_machine, move_user )

    who_won = ""
    draw = 0
    if( move_win == move_machine):
        who_won = "machine"
    elif(move_win == draw):
        who_won = "draw"
    else:
        who_won = "user"

    move_machine_name = full_name_moves[move_machine - 1]
    move_user_name = full_name_moves[move_user - 1]


    print()
    print("- " * 50)
    print()
    print("Machine move as '{}' and you move as '{}'".format(move_machine_name, move_user_name))

    if(who_won == "user"):
        print("You won!")
    elif(who_won == "draw"):
        print("Draw!")
    else:
        print("Machines won!")


else:
    print("It isn't a invalid move")
