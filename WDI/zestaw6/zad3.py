c=0
def rek(T,k,w=0,suma=T[w][k]):
	global c
	if w==7:
		if c==0 or c>suma:
			c=suma
		return
	rek(T,k,w+1,suma+T[w+1][k])
	if k-1>=0:
		rek(T,k-1,w+1,suma+T[w+1][k-1])
	if k+1<=7:
		rek(T,k+1,w+1,suma+T[w+1][k+1])

szach=[[41,21,7,5,23,98,31,17],
[41,21,7,5,23,98,31,17],
[41,21,7,5,23,98,31,17],
[41,21,7,5,23,98,31,17],
[41,21,7,5,23,98,31,17],
[41,21,7,5,23,98,31,17],
[41,21,7,5,23,98,31,17],
[41,21,7,5,23,98,31,17],]

rek(szach,4)

print(c)

