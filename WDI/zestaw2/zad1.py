from math import*

def fb(n):
    a=1
    b=1
    if n==1:
        return a
    if n==2:
        return b
    else:
        while n>2:
            tmp=a+b
            a=b
            b=tmp
            n-=1
        return b
def isF(y):
    j=1
    while True:
        if fb(j)==y:
            return True
        if fb(j)>y:
            return False
        j+=1
def exc(x):
    s=int(sqrt(x))+1
    for i in range(1,s):
        if x%i==0 and isF(i) and isF(x/i):
            return True
    return False
pr=[104,22,169,49,1220,2137]
for k in pr:
    if exc(k):
        print(k)
    
