# Title
def Yes_No(question):
    while True:
        # Instructions
        # Asks the user if they want to read the instructions
        response = input(question).lower()
        if response == 'yes' or response == 'y':
            print('You chose Yes')
        elif response == 'no' or response == 'n':
            print("You chose no")
        else:
            print('Choose either yes or no')


def instructions():
    print('''
    
*** instructions ***

To begin, decide the overall score needed to be crowned the winner of the game (eg: first person to
get a score of 50 or more).
At the start of each round, the user and the computer each roll two dice. The initial number of
points for each player is the total shown by the dice. Then, taking turns, the user and computer each
roll a single die and add the result to their points. The goal is to get 13 points (or slightly less) for a
given round. Once you are happy with your number of points, you can ‘pass’.
- If you go over 13, then you lose the round (and get zero points).
- If the computer goes over 13, the round ends and your score is the number of points that
you have earned.
- If the computer gets more points than you (eg: you get 10 and they get 11, then you lose
your score stays the same).
- If you get more points than the computer (but less than 14 points), you win and add your
points to your score. The computer’s score stays the same.
- If the first roll of your dice is a double, then your score is increased by double the number of
points, provided you win. If the computer’s first roll of the dice is a double, then its points
are not doubled (this gives the human player a slight advantage).
- The ultimate winner of the game is the first one to get to the specified score goal.

''')


# Main Routine
print()
print('🎲 Roll it 13 🎲')
print()

want_instructions = input('Do you want to read the instructions? ').lower()
if want_instructions == 'yes' or want_instructions == 'y':
    instructions()
elif want_instructions == 'no' or want_instructions == 'n':
    print('You chose No')
else:
    print("Choose either Yes or No")



