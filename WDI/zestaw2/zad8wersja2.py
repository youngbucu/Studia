def sb(n):
    w=0
    a=1
    b=1
    while n>0:
        w+=a
        tmp=a
        a=b
        b=tmp+b
        n-=1
    return w

def pdc(n,k):
    return sb(k)-sb(n-1)

def ow(n):
    a=1
    while pdc(a,a)<n:
        a+=1
    return a

def main():
    n=int(input("Podaj liczbę naturalną z przedziału (0,1000): "))
    n=n+1
    while True:
        e=0
        for i in range(1,ow(n)):
            for j in range(i+1,ow(n)):
                if pdc(i,j)==n:
                    e=1
        if e==0:
            print(n)
            break
        n+=1

if __name__=="__main__":
    main()

                




