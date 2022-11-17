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

def main():
    n=int(input("Podaj liczbę naturalną z przedziału (0,1000): "))
    l=1
    p=1
    while True:
        while sb(p)<n+1:
            while sb(l+p-1)-sb(p-1)<n+1:
                if sb(l+p-1)-sb(p-1)==n+1:
                    break
                l+=1
            if sb(l+p-1)-sb(p-1)==n+1:
                break
            l=1
            p+=1
        if sb(l+p-1)-sb(p-1)==n+1:
            print(n+1)
            break
        n+=1


if __name__=="__main__":
    main()
