def pz(n,k):
	s=[]
	for i in range(1,k+1):
		s.append(i)
	print(ts(s))
	for i in range(1,m.comb(n,k)):
		j=-1
		while True:
			if j==-1 and s[j]<n:
				s[j]=s[j]+1
				print(ts(s))
				break
			else:
				while True:
					j=j-1
					if s[j+1]-s[j]>1:
						s[j]=s[j]+1
						while j<-1:
							s[j+1]=s[j]+1
							j+=1
						break
				print(ts(s))
				break