def quicksort(A):
      if len(A) < 2:
          return A
      else:
          x = A[0]
          less = [i for i in A[1:] if i[0] <= x[0]]
          greater = [i for i in A[1:] if not i[0] <= x[0]]
          return quicksort(greater) + [x] + quicksort(less)
          
def quicksort1(A):
    if len(A) < 2:
        return A
    else:
        x = A[0][0]
        i = 0
        for j in range(len(A)-1):
            if A[j+1][0] <= x:
                A[j+1],A[i+1] = A[i+1], A[j+1]
                i += 1
        A[0],A[i] = A[i],A[0]
        less = quicksort1(A[:i])
        greater = quicksort1(A[i+1:])
        return greater + [A[i]] + less
		
def maximumbasis(A):
	from fractions import Fraction
	n=len(A)
	m=len(A[0])
	G=[]
	if n==1:
		return({1},G[0][1])
		
	for i in range(n):
		a=0
		for j in range(m):
			a+=A[i][j]
		G.append([a,i])	
		
	G=quicksort1(G)
	
	
	
	if G[0][0]==0:
		return (set(),Fraction(0,1))
		
	
	M1=[G[0]]
	M2=[A[G[0][1]]]
	result1=set()
	result2=0
	start=0
	while M2[0][start]==0:
		start+=1
	M3=[start]
	
		
		
	for j in range(1,n):
		X=[]
		M2.append([])
		start=0
		for i in range(len(M1)):
			x=0	
			for k in range(len(X)):
				x+= -X[k]*M2[k][i]
			x=(x- A[G[j][1]][M3[i]])/M2[i][M3[i]]
			X.append(x)
		for l in range(m):
			b=A[G[j][1]][l]
			for h in range(len(X)):
				b+=X[h]*M2[h][l]
			M2[j].append(b)
		if M2[j]==[0]*m:
			M2=M2[:j]
			continue
		while M2[j][start]==0:
			start+=1
		M3.append(start)
		M1.append(G[j])
		if len(M2)==m:
			for g in range(m):
				result1.add(M1[g][1]+1)
				result2+=M1[g][0]
			return (result1, result2)
		

	for g in range(len(M2)):
		result1.add(M1[g][1]+1)
		result2+=M1[g][0]
	return (result1, result2)
			
			
