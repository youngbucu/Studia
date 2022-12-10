import math as m

def isPrime(n):
	if n==2:
		return True
	for i in range(2,int(m.sqrt(n))+1):
		if n%i==0 or n==1 or n==0:
			return False
	return True

def bin(n,k):
	res=''
	while n>0:
		res+=str(n%2)
		n=n//2
	while len(res)!=k:
		res+='0'
	return res[::-1]

def main():
	a=str(input("Podaj pierwszą liczbę: "))
	b=str(input("Podaj drugą liczbę: "))
	d=len(a)+len(b)
	m=2**(d)
	for i in range(0,m):
		x=bin(i,d)
		if x.count('0')==len(a):
			wyn=''
			ia=0
			ib=0
			for j in x:
				if j=='0':
					wyn+=a[ia]
					ia+=1
				else:
					wyn+=b[ib]
					ib+=1
			if isPrime(int(wyn)):
				print(wyn)

if __name__=='__main__':
	main()