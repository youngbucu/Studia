x=int(input("Podaj sumę: "))
def fib(n):
    a=1
    b=1
    if n==1 or n==2:
        return a
    else:
        for i in range(2,n):
            tmp=a
            a=b
            b=b+tmp
        return b
def df(k):
    n=1
    while fib(n)<k:
        n+=1
    return n
z=0
print("Dlugosc: ",df(x))
for i in range(1,df(x)):
    s=fib(i)
    for j in range(i+1,df(x)):
        s=s+fib(j)
        print(s)
        if s==x:
            z=1
if z==1:
    print("Tak")
else:
    print("Nie")
        

        


        
        
        
            

    
    
