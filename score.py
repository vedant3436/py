#a program to prompt for a score between 0 and 10.0 and give Grade according to the score.
#If the score is out of range, print an error message

score = input('Enter Your Score: ')
try:
    new_score = float(score)
    if new_score>10.0:
        print('Enter A Score Between 0 to 10.0 range')
    elif new_score>=9.0:
        print('A')
    elif new_score>=8.0:
        print('B')
    elif new_score>=7.0:
        print('C')
    elif new_score>=6.0:
        print('D')
    else:
        print('Bad Score')
except:
    print('Enter a numerical value as your score!')
