n=int(input("Podaj liczbę naturalną: "))
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
k=2
while True:
    il=n/fib(k)
    r=n%fib(k)
    if il<1:
        print("Nie")
        break
    if r==0 and (il==fib(k-1) or il==fib(k+1)):
        print("Tak")
        break
    k+=1

    

