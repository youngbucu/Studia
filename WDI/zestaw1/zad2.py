wd=0
ws=10000
for i in range(1012,2022):
    a=2022
    b=i
    ts=0
    while a>b:
        tmp=a
        a=b
        b=tmp-b
    ts=a+b
    print("wyraz",i,"suma:",ts)
    if ws>ts:
        ws=ts
        wd=i

c=2022
print(c)
print(wd)
while c>wd:
    tmpp=c
    c=wd
    wd=tmpp-wd
    print(wd)




        



            
