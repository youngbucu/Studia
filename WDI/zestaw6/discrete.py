w=0
for i in range(2,21):
	for j in range(0,21-i,2):
		for k in range(0,6-i-j):
			w+=1
print(w)