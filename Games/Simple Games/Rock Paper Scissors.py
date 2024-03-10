import random

choices = ['rock', 'paper', 'scissors']

userScore = 0
compScore = 0

userChoice = input(f'From {choices} choose one:')
compChoice = random.choice(choices)

print(f'You chose {userChoice}. CPU chose {compChoice}')

while userScore != 3 or compScore != 3:
    if userScore == 3:
        print('Player wins best out of 3.')
        break

    if compScore == 3:
        print('CPU wins best out of 3.')
        break

    # rock
    if userChoice.lower() == 'rock':
        if compChoice == 'scissors':
            print('You win!')
            userScore += 1
        elif compChoice == 'rock':
            print('Tie!')
        elif compChoice == 'paper':
            print('You lose!')
            compScore += 1

    # paper
    elif userChoice.lower() == 'paper':
        if compChoice == 'rock':
            print('You win!')
            userScore += 1
        elif compChoice == 'paper':
            print('Tie!')
        elif compChoice == 'scissors':
            print('You lose!')
            compScore += 1

    # scissors
    elif userChoice.lower() == 'scissors':
        if compChoice == 'paper':
            print('You win!')
            userScore += 1
        elif compChoice == 'scissors':
            print('Tie!')
        elif compChoice == 'rock':
            print('You lose!')
            compScore += 1
