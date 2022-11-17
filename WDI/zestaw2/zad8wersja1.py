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

def pdc(x):
    z=0
    for i in range(1,df(x)):
        s=fib(i)
        for j in range(i+1,df(x)):
            s=s+fib(j)
            if s==x:
                z=1
    if z==1:
        return False
    else:
        return True

def main():
    n=int(input("Podaj liczbę naturalną z przedziału (0,1000): "))
    while True:
        if pdc(n+1):
            print(n+1)
            break
        n+=1

if __name__=="__main__":
    main()
