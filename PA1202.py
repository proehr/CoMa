from fractions import Fraction
from copy import deepcopy 

def maximumbasis(A):
	
	m=len(A)
	n=len(A[0])
	
	W=[]
	Q=[]
	for i in range(m):
		w=0
		for j in range(n):
			w+=A[i][j]
		W.append(w)	
		Q.append(w)
		
	C=quicksort(W)

	D=[]											
	for i in range(m):
		a=Q.index(C[i])
		D.append(A[a])
		Q[a]=-1

	
	E=greedy(D)											
	l=len(E)
	F=set()
	f=0
	for i in range(l):
		b=A.index(E[i])
		F.add(b+1)
		f+=W[b]
	
	return ((F, f))
				

def greedy(B):
	
	X=[] 
	Y=[]
	Z=[] 
	n=len(B[0])
	m=len(B)
		
	for i in range(n):
		Y.append([])
		
	for i in range(m):
	
		for j in range(n):
			Y[j].append(B[i][j])
			
		
		if len(Y)<len(Y[0]):
			break
		
		if gauss(Y):
			X.append(B[i])
			Z=Y			
		else:
			Y=Z
			
	return X
			
	
def gauss(A):
	A=deepcopy(A)
	G=[]
	m=len(A[0])
	n=len(A)
			
	for j in range(m):	
		
		for i in range(j):
			G[i].append(0)

		for i in range(j,n):
						
			if i<m:	
				if A[i][i]==0:
					for k in range(i+1,n):
						if A[k][i]!=0:
							A[i], A[k]=A[k], A[i]
							break	
					if A[i][i]==0:
						return False
																 
			if j==0:
				G.append([])
				
			if j<i:
				
				X=[]
				for k in range(0,j):
					X.append(A[i][k])
					
				for k in range(j,m):
					X.append(Fraction(A[i][k]-(A[i][j]/A[j][j]*A[j][k])))
				A[i]=X
				
			else:
				G[i].append(A[i][j])
								
	return True

def quicksort(A):
      if len(A) < 2:
          return A
      else:
          x = A[0]
          less = [i for i in A[1:] if i <= x]
          greater = [i for i in A[1:] if not i <= x]
          return quicksort(greater) + [x] + quicksort(less)
