def ist_aequivalenzrelation(n,R):
		alist=[]
				
		for i in range(1,n+1):
			alist.append([])
		
		for i in range(0,len(R)):
			if R[i][0]>n or R[i][1]>n:
				return False
			else:
				(alist[R[i][0]-1]).append(R[i][1])
			
		for x in alist:
			x.sort()
			
		for i in range(0,n):
			if i+1 not in alist[i]:
				return False
				
		for j in range(0,n):
			for k in range(0,len(alist[j])):
				for l in range(j+1,n):
					if alist[j][k] in alist[l]:
						if set(alist[j])!=set(alist[l]):
							return False
						else:
							alist[l]=[]
							
		return True				
			
		
		

					
		
	
		
	
