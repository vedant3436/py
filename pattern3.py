def p(n):
    b=n+1
    for i in range(n): 
        b=b-1
        num = list(reversed(range(b,n+1)))
        num_Str=map(str,num)
        print(" ".join(num_Str))

p(int(input('Enter input: ')))