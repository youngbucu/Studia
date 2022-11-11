def bubbleSort(a):
	n=len(a)
	swapped=False
	for i in range(n-1):
		for j in range(0,n-i-1):
			if a[j]>a[j+1]:
				swapped=True
				a[j], a[j+1]=a[j+1], a[j]
		if not swapped:
			break
	return a


def main():
	t=[]
	while True:
		n=int(input("Podaj liczbę: "))
		if n==0:
			break
		t.append(n)
	t=bubbleSort(t)
	print(t[-10])


if __name__=="__main__":
	main()
