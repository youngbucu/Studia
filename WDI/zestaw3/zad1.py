def main():
	n=int(input("Podaj liczbę naturalną: "))
	p=int(input("Podaj podstawę: "))
	w=''
	while True:
		r=n%p
		if r==10:
			w+="A"
		elif r==11:
			w+="B"
		elif r==12:
			w+="C"
		elif r==13:
			w+="D"
		elif r==14:
			w+="E"
		elif r==15:
			w+="F"
		else:
			w+=str(r)
		n=n//p
		if n==0:
			break
	print(w[::-1])

if __name__=="__main__":
	main()




