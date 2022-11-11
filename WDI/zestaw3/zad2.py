def main():
	a=int(input("Podaj liczbę naturalną: "))
	b=int(input("Podaj drugą liczbę naturalną: "))
	if set(str(a))==set(str(b)):
		print("TAK")
	else:
		print("NIE")

if __name__=="__main__":
	main()