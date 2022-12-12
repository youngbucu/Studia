import math as m
tab=[]
def isPrime(n):
	if n==2:
		return True
	if n<2:
		return False
	for i in range(2,int(m.sqrt(n))+1):
		if n%i==0:
			return False
	return True

def zmn(n):
	if isPrime(n):
		res=1
	else:
		res=0
	for i in range(2,(n//2)+1):
		if n%i==0 and isPrime(i):
			res+=1
	return res

def rek(T):
	global tab
	if len(T)==0:
		return
	tab.append(zmn(T[0]))
	del T[0]
	rek(T)
	if len(set(tab))==3:
		return True
	else:
		return False



lista=[2,8,64,56,117,30,66,1045]
if rek(lista):
	print('siema')


