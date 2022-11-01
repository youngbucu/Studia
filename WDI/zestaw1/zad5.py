n=int(input("Podaj liczbę naturalną: "))
a=1
b=n
e=0.00001
while abs(a-b)>e:
    a=(a+b)/2
    b=n/a
print(a,b)
