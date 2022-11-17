import random as r
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
	n=int(input("Podaj długość tablicy: "))
	t=[]
	for i in range(n):
		t.append(r.randrange(1,1000))
	print(t)
	x=len(t)-1
	if czp(x) and t[0]%x==0:
		print("Tak")
	else:
		print("Nie")

if __name__=="__main__":
	main()