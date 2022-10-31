a=2
b=2
print(a)
print(b)
while b<1000000:
    tmp=a
    a=b
    b=b+tmp
    print(b)

