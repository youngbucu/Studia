def main():
    n=int(input("Podaj liczbę cyfr: "))
    p=10**(n-1)
    k=''
    for j in range(n):
        k+='9'
    
    for i in range(p,int(k)+1):
        w=0
        s=str(i)
        for z in s:
            w+=(int(z))**3
        if int(i)==w:
            print(i)
    print("Koniec")
    
if __name__=="__main__":
    main()
    