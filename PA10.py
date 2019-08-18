def LR_decomposition(M):
	M=M.split(', ')
	L=[]
	n=len(M)
	for i in range(n):						##Liste für M und L Erstellen, L hat 1 auf ii, sonst 0
		M[i]=M[i].split(' ')
		L.append([])
		for j in range(n):
			M[i][j]=int(M[i][j])
			if j==i:
				L[i].append(1)
			else:
				L[i].append(0)
				
	from copy import deepcopy				##Liste L kopieren, aber tatsächlich neu anlegen, deswegen deepcopy
	LR=deepcopy(L)			
	LAlt=deepcopy(L)		
	for i in range(0,n-1):
		if M[i][i]==0:						##Überprüfen ob zu untersuchende Zeile in relevanter Spalte eine Null hat
			x=i								
			while M[x][i]==0 and x<n:
				x+=1
			M[i],M[x]=M[x],M[i]				##wenn ja, mit nächster Zeile, die in relevanter Spalte keine Null hat, austauschen
		for j in range(i+1,n):				
			L[j][i]=-M[j][i]/M[i][i]		##Werte unterhalb der aktuellen Zeile für L definieren
			LR[j][i]=str(int(-L[j][i]))		##Für LR umformen, sodass die Werte gespeichert werden
		M=mply(L,M)							##M und L multiplizieren, M ist also am Ende der Schleife das gesuchte R
		L=deepcopy(LAlt)					##L wieder auf Originalzustand zurückführen
	
	for i in range(n):						##alle Werte auf und über Diagonale durch Werte aus M ersetzen
		for j in range(i,n):
			LR[i][j]=str(int(M[i][j]))
			
	x=''									##Liste wieder zu String umformen 
	for i in range(n):
		for j in range(n):
			x = x + LR[i][j] + ' '
		x=x[:-1] + ', '
	x=x[:-2]
	
	return x
		
		
		
		
def mply(X,Y):								##Funktion für Multiplikation von Matrizen in Listenform, Rückgabe in Listenform
	R=[]
	for i in range(len(X)):
		R.append([])
		for j in range(len(X)):
			r=0
			for k in range(len(X)):
				r += X[i][k] * Y[k][j]
			R[i].append(r)
			
	return R
	


			
		

