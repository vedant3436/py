#a program(but with the help of function) to prompt for a score between 0 and 10.0 and give Grade according to the score.
#If the score is out of range, print an error message

def computescore(new_score):
    if new_score>10.0:
        return 'Enter A Score Between 0 to 10.0 range'
    elif new_score>=9.0:
        return 'A'
    elif new_score>=8.0:
        return 'B'
    elif new_score>=7.0:
        return 'C'
    elif new_score>=6.0:
        return 'D'
    else:
        return 'Bad Score'

score = input('Enter your score: ')

try:
    num_score = float(score)
    x = computescore(num_score)
    print(x)
except:
    print('Enter a numerical value')
    quit()