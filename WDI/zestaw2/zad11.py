def main():
    n=int(input("Podaj liczbę naturalną: "))
    s=str(n)
    e=0
    for i in range(1,len(s)):
        if s[i]<s[i-1]:
            e=1
            break
    if e==1:
        print("Nie")
    else:
        print("Tak")

if __name__=="__main__":
    main()



    

