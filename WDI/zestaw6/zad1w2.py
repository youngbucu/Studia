import math as m
tab=[]
tab2=[]
def isPrime(n):
    if n==2:
        return True
    for i in range(2,int(m.sqrt(n))+3):
        if n%i==0 or n<2:
            return False
    return True

def ntol(n):
    t=[]
    for i in n:
        t.append(i)
    return t

def sklej(T):
    w=''
    for i in T:
        if i!='x':
            w+=i
    if w=='':
        return 0
    else:
        return int(w)
    
def rek(x):
    global tab, tab2
    if x==-1:
        if len(str(sklej(tab)))!=len(tab) and len(str(sklej(tab)))!=0 and isPrime(sklej(tab)):
            print(sklej(tab))
        else:
            return
    else:
        tab[x]=tab2[x]
        rek(x-1)
        tab[x]='x'
        rek(x-1)

def main():
    n=str(input("Podaj liczbę: "))
    global tab, tab2
    tab=ntol(n)
    tab2=ntol(n)
    rek(len(tab)-1)

if __name__ == "__main__":
    main()
        
    
    
        

