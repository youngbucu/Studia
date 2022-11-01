x=int(input("Podaj pierwszą liczbę: "))
y=int(input("Podaj drugą liczbę: "))
def nwd(a,b):
    if a>b:
        while True:
            r=a%b
            if r==0:
                return b
            else:
                a=b
                b=r
    else:
        while True:
            r=b%a
            if r==0:
                return a
            else:
                b=a
                a=r
def nww(c,d):
    return (c/nwd(c,d))*d
print("NWW:",int(nww(x,y)))
