import math as m

def main():
    n=int(input("Podaj liczbę naturalną: "))
    b=(n//2)+1
    a=2
    while True:
        if n%a==0:
            print("Tak")
            break
        elif a>b:
            print("Nie")
            break
        a=3*a+1

if __name__=="__main__":
    main()