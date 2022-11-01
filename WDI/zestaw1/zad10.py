import math as m
for i in range(2,1000000):
    suma=0
    for j in range(1,int(m.sqrt(i))+1):
        if i%j==0:
            suma+=j+(int(i/j))
    suma-=i
    if suma==i:
        print(i)
print("Koniec")
            
