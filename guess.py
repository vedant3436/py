'''A Guess the number game, but to make it more convenient i put in conditions at instances where the program
would give an error incase the user does not input a valid value, and when it does, it makes the person who 
wrote the program (me) look a bit unprofessional. So to avoid that, I put in a personal error message which 
solves that worry for me.
'''

import random

print("Choose a Range of numbers from which you would like to choose.")

try:
    a = int(input('Enter 1st Number: '))
    b = int(input('Enter 2nd Number: '))
    if a == b:
        print('Hey! that is not a valid range, now you gotta run the program again.')
        quit()
    elif a>b:
        y = a
        x = b 
    else:
        x = a 
        y = b  
except:
    print('Enter numbers only!')
    quit()

randNum = random.randint(x,y)

nGuess = 0 
guessNum = None 
while guessNum != randNum:
    nGuess += 1
    try:
        guessNum = int(input('Take your guess: '))
    except:
        print('Enter numbers only!')
        quit()
    if guessNum>randNum:
        print('Too High! Guess a smaller number.')
    else:
        print('Too Low! Guess a larger number.')

print(f'Great! You guessed the right number in {nGuess} guesses. It was {randNum}.')
