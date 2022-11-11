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
		while i+1+a<len(t) and t[i+a]<t[i+1+a]:
			a+=1
		if wd<a+1:
			wd=a+1
			pw=i
	print(wd,t[pw])



if __name__=="__main__":
	main()