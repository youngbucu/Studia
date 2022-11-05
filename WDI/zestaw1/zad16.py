def main():
	wp=0
	ww=0
	for i in range(2,10001):
		a=i
		p=0
		while a!=1:
			a=(a%2)*(3*a+1)+(1-(a%2))*a/2
			p+=1
		if wp<p:
			wp=p
			ww=i
	print(ww)


			




if __name__=="__main__":
	main()