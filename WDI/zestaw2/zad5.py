import math as m
def main():
	n=str(input("Podaj liczbę spełniająca warunki zadania: "))
	a=int(input("Podaj dzielnik: "))
	l=[]

	for j in range(0,len(n)):
		l.append(n[j])
	res=0
	for i in range(1,len(n)):
		for k in pz(len(n),i):
			tl=l.copy()
			num=''
			for z in range(0,len(k)):
				tl[int(k[z])-1]=0
			for x in tl:
				if x!=0:
					num+=x
			if int(num)%a==0:
				res+=1
				print(num)
	print("Odpowiedź:",res)


def ts(n):
	r=''
	for i in n:
		r+=str(i)
	return r


def pz(n,k):
	wynik=[]
	s=[]
	for i in range(1,k+1):
		s.append(i)
	wynik.append(ts(s))
	for i in range(1,m.comb(n,k)):
		j=-1
		while True:
			if j==-1 and s[j]<n:
				s[j]=s[j]+1
				wynik.append(ts(s))
				break
			else:
				while True:
					j=j-1
					if s[j+1]-s[j]>1:
						s[j]=s[j]+1
						while j<-1:
							s[j+1]=s[j]+1
							j+=1
						break
				wynik.append(ts(s))
				break
	return wynik

if __name__=="__main__":
	main()