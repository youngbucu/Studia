import math as m 
def main():
	a=int(input("Podaj pierwszą liczbę: "))
	b=int(input("Podaj drugą liczbę: "))
	for i in range(0,100000):
		tmp=a
		a=m.sqrt(a*b)
		b=(tmp+b)/2
	print(a,b)

if __name__=="__main__":
	main()