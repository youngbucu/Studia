def main():
    n=int(input("Podaj liczbę naturalną: "))
    s=str(n)
    e=0
    for i in range(0,len(s)):
        if int(s[i])==len(s):
            e=1
            break
    if e==1:
        print("Tak")
    else:
        print("Nie")

if __name__=="__main__":
    main()
