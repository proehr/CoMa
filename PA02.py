def quersummen(n):
	p=n
	a=str()
	for b in range(2,n+1):
		q=0
		i=0
		while b**i <= n:
			i += 1
		i-=1
		while i>(-1):
			j=0
			while j*(b**i) <= n:
				j += 1
			j-=1
			q+=j
			n= n-j*(b**i)
			i-=1
		n=p
		a=a+str(q)+" "
	a=a[:-1]
	print(a)
