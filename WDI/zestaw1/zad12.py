x=int(input("Podaj pierwszą liczbę: "))
y=int(input("Podaj drugą liczbę: "))
z=int(input("Podaj trzecią liczbę: "))
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
print("Nwd tych liczb to:",nwd(nwd(x,y),z))

        
        
        
            
        
