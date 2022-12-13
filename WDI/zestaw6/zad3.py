T=[]
c=0
def rek(k,suma,w=0):
	global T,c
	if w==7:
		if c==0 or c>suma:
			c=suma
		return
	if k-1>=0:
		rek(k-1,suma+T[w+1][k-1],w+1)
	if k+1<=7:
		rek(k+1,suma+T[w+1][k+1],w+1)
	rek(k+0,suma+T[w+1][k],w+1)

def main():
	global T,c
	szach=[[41,251,78,5,23,98,317,17],[65,21,145,5,273,98,31,17],[41,214,7,5,23,98,31,197],[41,21,7,5,23,98,371,17],[411,21,7,5,232,98,31,17],[41,21,77,5,23,928,31,17],[41,21,7,5,23,98,31,17],[41,211,7,5,23,98,361,17]]
	T=szach
	a=int(input("Podaj startową kolumnę: "))
	b=T[0][a]
	rek(a,b)
	print(c)

if __name__=='__main__':
	main()



