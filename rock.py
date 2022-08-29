'''A Simple Rock Papers Scissor game, if the user types anything
other than rock ,paper or scissor the program should not give an error but
it will print out an error message and terminate on it's own'''

import random

def rps(val,play):
    if val == play:
        return None
    elif val == 'r':
        if play == 'p':
            return True
        elif play == 's':
            return False
    elif val == 'p':
        if play == 'r':
            return False
        elif play == 's':
            return True
    elif val == 's':
        if play == 'r':
            return True
        elif play == 'p':
            return False

print('The Computer the choosing: Choose Rock(r), Paper(p) or Scissor(s)')

comp = random.randint(1,3)
if comp == 1:
    val = 'r'
elif comp == 2:
    val = 'p'
elif comp == 3:
    val = 's'

play = input('Your Turn: Choose Rock(r), Paper(p) or Scissor(s): ')
if play == 'r':
    pass
elif play == 'p':
    pass
elif play == 's':
    pass
else:
    print('Only Enter r or p or s!')
    quit()

res = rps(val, play)

print('Computer Chose, ' + val)
print('You Chose, ' + play)

if res == None:
    print('The Game is a Tie!') 
elif res:
    print('You Win!')
else:
    print('You Lost!')
