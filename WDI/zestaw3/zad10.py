import random as r

def main():
	wd=1
	pw=0
	n=int(input("Podaj długość tablicy: "))
	t=[]
	for i in range(n):
		t.append(r.randrange(1,1000))
	print(t)
	for i in range(0,len(t)):
		a=0
		while i+2+a<len(t) and (t[i+a]+t[i+2+a])/2==t[i+1+a]:
			a+=1
		if wd<a+2:
			wd=a+2
			pw=i
	if wd>2:
		print(wd,t[pw])
	else:
		print("Brak")



if __name__=="__main__":
	main()