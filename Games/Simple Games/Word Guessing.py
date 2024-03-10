import random

words = ['ADIEU', 'ACUTE', 'ARISE', 'AUDIO', 'AHEAD', 'ALLOW', 'ARGUE', 'BREAK', 'BRIEF', 'BAKER', 'COLOR', 'COUNT', 'CLAIM', 'DELAY', 'DOING', 'DREAM', 'DRESS', 'ELDER', 'EIGHT', 'EQUAL', 'EXACT', 'FAITH', 'FINAL', 'FRAME', 'FIELD',
         'GRADE', 'GRANT', 'GLOBE', 'HUMOR', 'HEART', 'HOUSE', 'IDEAS', 'INDEX', 'INPUT', 'JUDGE', 'LIVES', 'MAGIC', 'MAJOR', 'NOISE', 'ORDER', 'PIECE', 'QUITE', 'REACT', 'SOARE', 'SOUND', 'TEAMS', 'THOSE', 'WATER', 'WASTE', 'YOUNG']

word = random.choice(words)

lives = 6
tries = 0
win = False


def letterCheck(guess, word):
    if guess.lower()[0:1] == word.lower()[0:1]:
        print(f'{guess[0:1]} is in the right place.')
    if guess[1:2].lower() == word.lower()[1:2]:
        print(f'{guess[1:2]} is in the right place.')
    if guess[2:3].lower() == word.lower()[2:3]:
        print(f'{guess[2:3]} is in the right place.')
    if guess[3:4].lower() == word.lower()[3:4]:
        print(f'{guess[3:4]} is in the right place.')
    if guess[4:5].lower() == word[4:5].lower():
        print(f'{guess[4:5]} is in the right place.')
    else:
        print('Nothing else is in the word.')


while lives != 0 or win == False:
    guess = input("Enter your guess:\nMust be 5 letters.")
    if len(guess) != 5:
        print('The word length should be 5.')

    elif guess.lower() == word.lower():
        tries += 1
        print(f'You win! It took you {tries} tries.')
        win = True

    else:
        letterCheck(guess, word)
        lives -= 1
        tries += 1
        print(f'You have {lives} lives left!')
