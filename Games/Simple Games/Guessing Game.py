# Task:

# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random

lives = 10
tries = 0
win = False

A = int(input('Select starting range:'))
B = int(input('Select ending range:'))

if A >= B or (A + 20) >= B:
    print('The starting range must be at least 20 less than the end range.')

else:
    num = random.randint(A, B)
    while lives != 0 or win == False:
        if lives == 0:
            print(f'You lose!\nThe answer was {num}')
            break
        else:
            guess = int(input('What is your guess?'))
            if guess == num:
                tries += 1
                print(f'Correct! \nIt took you {tries} tries.')
                win = True
            elif guess >= num:
                lives -= 1
                tries += 1
                print(f'Guess is too high! \nYou have {lives} guesses left!')
            elif guess <= num:
                lives -= 1
                tries += 1
                print(f'Guess is too low! \nYou have {lives} guesses left!')
