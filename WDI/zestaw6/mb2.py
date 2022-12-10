ciag=[]

def mb(n):
    global ciag
    if n==0:
        print(ciag)
        print("koniec")
    else:
        ciag[-n]=0
        mb(n-1)
        ciag[-n]=1
        mb(n-1)

def main():
    n=int(input("Podaj ilosc elementow ciagu: "))
    global ciag
    ciag=[3 for _ in range(0,n)]
    mb(n)
   
if __name__ == "__main__":
    main()