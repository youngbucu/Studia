import random as r

def main():
	n=int(input("Podaj długość tablicy: "))
	t=[]
	for z in range(n):
		t.append(r.randrange(100,1000))
	for i in range(0,len(t)):
		for j in range