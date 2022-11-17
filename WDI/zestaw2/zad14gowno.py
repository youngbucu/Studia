import math as m

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

def zero(n):
    s=str(n)
    w=[0 for _ in range(len(s)*2+1)]
    d=0
    for i in range(1,len(w),2):
        w[i]=s[d]
        d+=1
    return w

def main():
    a=int(input("Podaj pierwszą liczbę"))


