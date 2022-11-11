import math as m

def main():
	n=int(input("Podaj dokładność w miejscach po przecinku: "))
	w=0
	l=10**n
	for i in range(0,n+1):
		w+=l//(m.factorial(i))
	r=w%(2*(10**n))
	print("2.",r)

if __name__=="__main__":
	main()

