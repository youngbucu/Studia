def main():
    n=int(input("Podaj liczbę naturalną: "))
    s=str(n)
    e=0
    for i in range(0,len(s)-1):
        if s[i]==s[len(s)-1]:
            e=1
            break
    if e==1:
        print("Nie")
    else:
        print("Tak")

if __name__=="__main__":
    main()