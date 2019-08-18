def aeklasse(n,R):
	alist=[]
	x=len(R)
	for i in range(0,x):
		if n==R[i][0]:
			alist.append(R[i][1])
	return alist
			
def ist_aequivalenzrelation(n,R):
	refl=True
	symm=True
	trans=True
	for i in range(1,n+1):
		if i in aeklasse(i,R):
			refl = refl
		else: 
			return False
		for j in aeklasse(i,R):
			if i in aeklasse(j,R):
				symm = symm
			else:
				return False
			for k in aeklasse(j,R):
				if k in aeklasse(i,R):
					trans = trans
				else:
					return False
	return refl and symm and trans
		
						
		
				
	
		
