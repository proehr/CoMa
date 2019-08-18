def repraesentant(a,m,k):
	for q in range (k,k+m):
		if (a-q)%m==0:
			return q
		else:
			q+=1
	
def f(z,l):
	return repraesentant(z,2**l,0)
	
def umkehrfunktion_von_f(r,l):
	return repraesentant(r,2**l,-2**(l-1))
