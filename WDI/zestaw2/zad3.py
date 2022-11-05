def main():
	n=int(input("Podaj liczbę naturalną: "))
	if str(n)==str(n)[::-1]:
		print("Liczba jest palindromem w systemie dziesiętnym")
	elif dw(n)==dw(n)[::-1]:
		print("Liczba jest palindromem w systemie dwójkowym")
	else:
		print("Liczba nie jest palindromem ani w systemie dziesiętnym ani dwójkowym")



def dw(n):
	w=''
	while n>0:
		w+=str(n%2)
		n=n//2
	return w[::-1]

if __name__=="__main__":
	main()