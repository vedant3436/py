#A program which repeatedly reads numbers until the user enters “done”.
#Once “done” is entered, print out the total, count and average of the numbers
#If the user enters anything other than a number,
#detect their mistake using try and except and print an errormessage and skip to the next number.

total = 0
count = 0

while True:
    totals = input('Enter a number,type done when you are finished: ')
    if totals == 'done':
        break
    try:
        total = float(totals) + total
        count = count + 1 
    except:
        print('Ente a numerical value')
        quit()

print('Total:',total)
print('Count:',count)

average = total/count
print(average)




