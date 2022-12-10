def mb(n):
	if n==0:
		print('\n')
		return
	else:
		print('0',end='')
		mb(n-1)
		print('1',end='')
		mb(n-1)
mb(3)

