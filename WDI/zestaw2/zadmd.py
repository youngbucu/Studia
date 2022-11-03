ciag=[]

def gp(n,p):
    global ciag
    print("gp",n,p,ciag)
    if n==p:
        for i in range(0,n):
            if ciag[i]==1:
                print(i+1)
        print("koniec")
    else:
        ciag[p]=0
        gp(n,p+1)
        ciag[p]=1
        gp(n,p+1)






def main():
    n=int(input("Podaj ilosc elementow ciagu: "))
    p=0
    global ciag
    ciag=[3 for _ in range(0,n)]
    gp(n,p)

    
        
if __name__ == "__main__":
    main()