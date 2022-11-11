import random as r

def main():
	n=int(input("Podaj długość tablicy: "))
	t=[]
	for i in range(n):
		t.append(r.randrange(1,1000))
	print(t)
	for j in t:
		x=str(j)
		found=True
		for k in x:
			if int(k)%2==0:
				found=False
			if not found:
				break
		if found:
			print("Tak bo",j)
			break
	if not found:
		print("Nie")



if __name__=="__main__":
	main()
