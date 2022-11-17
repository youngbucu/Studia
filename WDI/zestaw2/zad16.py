import math as m

def isPrime(n):
    if n==2:
        return True
    g=int(m.sqrt(n))
    for i in range(2,g+2):
        r=n%i
        if r==0 or n==1:
            return False
    return True

def sc(n):
    a=str(n)
    w=0
    for i in a:
        w+=int(i)
    return w

def main():
    for i in range(1,100000):
        a=i
        s=0
        for j in range(2,(a//2)+1):
            if a%j==0 and isPrime(j):
                while a%j==0:
                    s+=sc(j)
                    a=a/j
            if a==1:
                break
        if sc(i)==s:
            print(i)

if __name__=="__main__":
    main()


