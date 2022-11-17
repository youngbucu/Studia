import math as m

def czp(n):
	e=0
	for i in range(2,int(m.sqrt(n))+1):
		if n%i==0:
			e=1
	if e==1 or n==1 or n==0:
		return False
	else:
		return True

def main():
	n=int(input("Podaj koniec przedziału: "))
	t=[i for i in range(2,n+1)]
	for i in t:
		l=2
		if czp(i):
			while True:
				if l*i<=n:
					t[(l*i)-2]=0
					l+=1
				else:
					break
	w=[]
	for j in t:
		if j!=0:
			w.append(j)

	print(w)
	print("Koniec")




	
if __name__=="__main__":
	main()