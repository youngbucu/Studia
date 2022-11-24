def iloraz(t):
    w=0
    for x in range(0,len(t[1])):
        for y in range(0,len(t)):
            g=0
            licznik=0
            while True:
                if g<len(t):
                    licznik+=t[g][x]
                    g+=1
                else:
                    break
            mianownik=sum(t[y])
            if licznik/mianownik>w:
                w=licznik/mianownik
    return w

            