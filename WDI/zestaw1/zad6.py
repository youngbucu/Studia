def f(x):
    return (x**x)-2020
b=0.0001
x1=4
x2=5
x0=7
while abs(f(x0))>b:
    x0=(x1+x2)/2
    if f(x0)<0:
        x1=x0
    else:
        x2=x0
print(x0)
