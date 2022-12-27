def p(n):
    for i in range(n):
        l = []
        for j in range(i+1):
            l.append(str((n-j)))

        print(" ".join(l))

p(int(input("I: ")))

