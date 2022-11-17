def main():
	n=int(input("Podaj liczbę naturalną: "))
	p=int(input("Podaj podstawę: "))
	w=''
	t=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	while True:
		w+=t[n%p]
		n=n//p
		if n==0:
			break
	print(w[::-1])

if __name__=="__main__":
	main()