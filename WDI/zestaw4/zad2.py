def np(t):
	for i in t:
		for j in i:
			found=True
			a=str(j)
			for k in a:
				if int(k)%2==0:
					found=False
					break
			if found:
				break
			
				


