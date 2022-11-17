import math as m

def main():
    n=int(input("Podaj liczbę naturalną: "))
    b=(n//2)+1
    c=1
    while True:
        a=c**2+c+1
        if n%a==0:
            print("Tak")
            break
        elif a>b:
            print("Nie")
            break
        c+=1

if __name__=="__main__":
    main()

