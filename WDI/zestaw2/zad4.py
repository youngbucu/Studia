def main():
	n=int(input("Podaj koniec przedziału: "))
	w=1
	for i in range(1,n+1):
		a=i
		while a%2==0:
			a=a/2
		while a%3==0:
			a=a/3
		while a%5==0:
			a=a/5
		if a==1 and i%30==0:
			w+=1
	print(w)

if __name__=="__main__":
	main()


