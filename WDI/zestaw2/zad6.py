import math as m

def main():
    n=int(input("Podaj liczbę naturalną: "))
    l=int(m.sqrt(n))+1
    while True:
        r=n%l
        if r==0:
            print(l,int(n/l))
            break
        l-=1

if __name__=="__main__":
    main()
    

