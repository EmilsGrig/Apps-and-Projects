player1 = input('Enter player 1\'s name:')
player2 = input('Enter player 2\'s name:')

numbers = []
numCur = 0
win = False

print(f'List is {numbers}')

while numCur != 21 or win == False:
    num1 = int(input(f'{player1}, How many numbers do you want?\nMaximum 3.'))
    if num1 > 3:
        num1 = 3
    elif num1 <= 0:
        num1 = 1

    for i in range(0, num1):
        numCur += 1
        numbers.append(numCur)
        print(f'List is {numbers}')

    if numCur >= 21:
        print(f'Winner is {player2}')

    num2 = int(input(f'{player2}, How many numbers do you want?\nMaximum 3.'))

    if num1 > 3:
        num1 = 3
    elif num1 <= 0:
        num1 = 1

    for i in range(0, num1):
        numCur += 1
        numbers.append(numCur)
        print(f'List is {numbers}')

    if numCur >= 21:
        print(f'Winner is {player1}')
        win = True
