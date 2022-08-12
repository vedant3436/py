#the following program will compute a pay of a worker depending upon how much time the worker has worked.
#if the work time is more than 40 hours (not equal to), the worker gets 1.5 times the usual pay. if not, the worker gets the regular payment
#the variable rate is changable without affecting the rest of the program

rate = 10
hours = input('Enter Hours worked: ')
try:
    new_hours = float(hours)
    if new_hours>40:
        pay = new_hours*(rate*1.5)
    else:
        pay = new_hours*rate
    print(pay)
except:
    print('Enter a Numerical Value')
