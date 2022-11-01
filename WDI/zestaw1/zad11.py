import math as m
for i in range(2,1000000):
    s1=0
    s2=0
    for j in range(1,int(m.sqrt(i))+1):
        if i%j==0:
            s1+=j+(int(i/j))
    s1-=i
    if s1<1000000 and i<s1:
        for k in range(1,int(m.sqrt(s1))+1):
            if s1%k==0:
                s2+=k+(int(s1/k))
    s2-=s1
    if s2==i and i!=s1:
        print(i,s1)

    
        
        

    
            
