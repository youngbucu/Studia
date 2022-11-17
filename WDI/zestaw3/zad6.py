import random as r

def main():
	n=int(input("Podaj długość tablicy: "))
	t=[]
	for i in range(n):
		t.append(r.randrange(1,1000))
	print(t)
	for j in t:
		x=str(j)
		found=False
		for k in x:
			if int(k)%2==1:
				found=True
			if found:
				break
		if not found:
			print("Nie bo",j)
			break
	if found:
		print("Tak")



if __name__=="__main__":
	main()
