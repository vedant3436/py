sum = 0 
sum1 = []
while True:
    a = input("Enter price, press q to quit: ")
    if a!='q':
        sum += int(a)
        sum1.append(a)
    else:
        print(f"thanks for using our calculator {sum} is your total bill.")
        break
    
print("Reciept")
for a,i in enumerate(sum1,1):
    print(f"{a}. {i}")


