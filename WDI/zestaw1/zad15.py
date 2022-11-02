import math as m
n=int(input("Podaj dokładność: "))
s=m.sqrt(0.5)
w=m.sqrt(0.5)
for i in range(0,n):
    s=m.sqrt(0.5+0.5*s)
    w=w*s
print(2/w)
