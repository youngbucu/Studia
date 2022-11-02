a=int(input("Podaj pierwszy wyraz: "))
b=int(input("Podaj drugi wyraz: "))
while b<1000000:
    tmp=a
    a=b
    b=b+tmp
print(b/a)
