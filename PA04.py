def f(n):
	a=0
	b=1
	for i in range(n):
		a,b=b,a+b
	return a

def goldener_schnitt(praezision):
	l=2
	while praezision >= f(2*l-3)*f(2*l-2):
		l+=1
	l-=1
	plist=[l,(f(2*l),f(2*l-1)),(f(2*l+1),f(2*l))]
	return plist
