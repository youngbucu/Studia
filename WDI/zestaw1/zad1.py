a=1
b=1
print(a)
print(b)
while b<1000000:
    tmp=a
    a=b
    b=b+tmp
    print(b)

