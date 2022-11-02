import math as m
a=float(input("Podaj argument: "))
b=int(input("Podaj dokładność: "))
def cos(x,n):
    s=1
    for i in range(1,n+1):
        if i%4==1:
            s+=0
        if i%4==2:
            s-=(1/m.factorial(i))*(x**i)
        if i%4==3:
            s+=0
        if i%4==0:
            s+=(1/m.factorial(i))*(x**i)
    return s
print("Wartość cos(x) dla podanego argumentu:",cos(a,b))


            
    
