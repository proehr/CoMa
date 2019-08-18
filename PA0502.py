def aeklasse(n,R):
	alist=[]
	x=len(R)
	for i in range(0,x):
		if n==R[i][0]:
			alist.append(R[i][1])
	alist.sort()
	return alist

def ist_aequivalenzrelation(n,R):
		a=True
		
		if n==1:
			if 1 in aeklasse(n,R):
				return True
			else:
				return False
				
		
			
		for i in range(1,n+1):
			for j in range(0,len(aeklasse(i,R))):
				for k in range(i+1,n+1):
					if aeklasse(i,R)[j] in aeklasse(k,R):
						if set(aeklasse(i,R))==set(aeklasse(k,R)):
							a=True
						elif set(aeklasse(i,R))!=set(aeklasse(k,R)):
							return False
		return a
		

					
		
	
		
	
