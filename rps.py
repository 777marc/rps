print()
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

if int(playerchoice) < 1 | int(playerchoice) > 3:
    print('invalid choice');

if int(playerchoice) == 1:
    print('you selected Rock')

if int(playerchoice) == 2:
    print('you selected Paper')

if int(playerchoice) == 1:
    print('you selected Scissor')