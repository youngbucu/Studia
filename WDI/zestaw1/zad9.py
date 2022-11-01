import math as m
n=int(input("Podaj liczbę: "))
for i in range(1,int(m.sqrt(n))+1):
    if n%i==0:
        print(i)
        print(int(n/i))
