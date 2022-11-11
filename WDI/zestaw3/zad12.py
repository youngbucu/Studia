import random as r

def main():
	n=int(input("Podaj długość tablicy: "))
	t=[]
	wdd=0
	wdu=0
	pwd=0
	pwu=0
	for z in range(n):
		t.append(r.randrange(1,99,2))
	f=126
	for m in range(7):
		f=f-14
		t.append(f)
	print(t)

	for i in range(0,len(t)):
		a=0
		while i+2+a<len(t) and t[i+a]<t[i+1+a] and(t[i+a]+t[i+2+a])/2==t[i+1+a]:
			a+=1
		if wdd<a+2:
			wdd=a+2
			pwd=i
	if wdd>2:
		print(wdd,t[pwd])
	else:
		print("Brak")

	for j in range(0,len(t)):
		b=0
		while j+2+b<len(t) and t[j+b]>t[j+1+b] and(t[j+b]+t[j+2+b])/2==t[j+1+b]:
			b+=1
		if wdu<b+2:
			wdu=b+2
			pwu=j
	if wdu>2:
		print(wdu,t[pwu])
	else:
		print("Brak")
	


if __name__=="__main__":
	main()