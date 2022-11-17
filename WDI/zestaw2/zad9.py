
def f(x):
    return 1/x

def main():
    a=float(input("Podaj początek przedziału:"))
    b=float(input("Podaj koniec przedziału:"))
    c=int(input("Podaj liczbę prostokątów:"))
    w=0
    dl=(b-a)/c
    for i in range(c):
        w+=f(a)*dl
        a+=dl
    print(w)

if __name__=="__main__":
    main()


    
