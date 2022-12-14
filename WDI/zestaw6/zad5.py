import math as m

T=[]
found=False
overflow=False

def bd(n):
    wynik=0
    p=len(str(n))-1
    for i in str(n):
        wynik+=int(i)*(2**p)
        p-=1
    return wynik
        
def isPrimeB(n):
    n=bd(n)
    if n==2:
        return True
    if n<2:
        return False
    for i in range(2,int(m.sqrt(n))+1):
	    if n%i==0:
		    return False
    return True

def rek(i=0):
    global T, found
    if i==len(T):
        found=True
        return
    l=''
    while True:
        l+=str(T[i])
        i+=1
        if len(l)==30:
            overflow=True
            return
        if isPrimeB(int(l)):
            print(l)
            rek(i)
        if i==len(T) or found or overflow:
            return

def main():
    global T
    T=[1,1,1,1,1]
    rek()
    print(found)

if __name__=='__main__':
    main()
            
        
    
        

    


