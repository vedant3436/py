''' A program that prompts user to enter marks obtained in Physics,Chemistry,Mathematics,
English and Computer Science. The program will go through the marks entered and passing marks are 33 out of 100 minimum 
for individual subject and overall 40% is minimum for a overall Pass result.
'''

mark_math_org = (input('Enter your Mathematics marks: '))
mark_phy_org= (input('Enter your Physics marks: '))
mark_chem_org = (input('Enter your Chemistry marks: '))
mark_eng_org= (input('Enter your English marks: '))
mark_cs_org = (input('Enter your Computer Science marks: '))

try:
    mark_math =  int(mark_math_org)
    mark_phy = int(mark_phy_org)
    mark_chem = int(mark_chem_org)
    mark_eng = int(mark_eng_org)
    mark_cs = int(mark_cs_org)
    if mark_math >= 33 and mark_phy >= 33 and mark_chem >= 33 and mark_eng >= 33 and mark_cs >= 33:
        if mark_math+mark_phy+mark_chem+mark_eng+mark_cs >= 200: #since 200 out of 500 is 40% overall
            print('Your Result is: Pass')
        else:
            print('Your Result is: Fail')
    else:
        print('Your Result is: Fail')
except:
    print('Enter Numerical Values only')