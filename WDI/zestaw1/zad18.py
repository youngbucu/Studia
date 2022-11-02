n=int(input("Podaj liczbę naturalną: "))
a=1
b=1
c=n
e=0.00000001
k=0
while abs(a-c)>e:
    a=(a+b+c)/3
    k=n/a
    b=(b+c)/2
    c=k/b
print(a,b,c)
