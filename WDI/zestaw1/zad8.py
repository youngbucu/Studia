import math as m
x=int(input("Podaj liczbę: "))
def isPrime(n):
    if n==2:
        return True
    g=int(m.sqrt(n))
    for i in range(2,g+2):
        r=n%i
        if r==0 or n==1:
            return False
    return True
if isPrime(x):
    print("Liczba pierwsza")
else:
    print("Liczba złożona")
    
