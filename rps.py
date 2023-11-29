import sys
import random

print()
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

if int(playerchoice) < 1 | int(playerchoice) > 3:
    print('invalid choice');

if int(playerchoice) == 1:
    print('you selected Rock')

if int(playerchoice) == 2:
    print('you selected Paper')

if int(playerchoice) == 3:
    print('you selected Scissor')

computerchoice = random.choice('123')

def get_name(selection):
    
    if selection == 1:
        return 'Rock'

    if selection == 2:
        return 'Paper'

    if selection == 3:
        return "Scissors"

def get_winner(player, computer):

    if player == 1 and computer == 1:
        return "Tie!"
    if player == 1 and computer == 2:
        return "You lose, paper beats rock."
    if player == 1 and computer == 3:
        return "You win!  Rock beats Scissors."

print(get_name(int(computerchoice)))
    
print(get_winner(int(playerchoice), int(computerchoice)))
