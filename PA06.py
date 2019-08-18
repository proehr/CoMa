def eulertour(A):
	if len(A)==0:    ##Spezialfall leere Liste
		return []
	
	for i in range (0,len(A)):  ##Überprüfen ob Grad jedes Knotens gerade ist
		if len(A[i])%2==1:
			return False		##falls nicht, keine Eulertour
	
	c=0
	while A[c]==[] and c<len(A)-1: ##erste nichtleere Liste in R finden, um erste Kante betrachten zu können: c
		c+=1
	if A[c]==[]:				##falls alles leere Listen, Eulertour vorhanden, aber leer
		return []
		
	blist=[c]					##blist ist Liste, die Eulertour enthalten soll, beginnt immer mit Knoten c
	for i in range (c,len(A)): 	##für jeden Knoten nach c im Graphen überprüfen ob in blist
		if i in blist:
			alist=[]
			a=i
			b=i
			while A[a]!=[]:		##solange Liste in der wir uns befinden nicht leer ist, Kanten ablaufen
				alist.append(a)	
				a=A[a].pop(0)	
				A[a].remove(b)
				b=a
			d=blist.index(i)
			blist=blist[:d] + alist + blist[d:]
			
	for i in range(0,len(A)):	##falls eine der Listen nicht leer ist, ist Graph nicht zusammenhängend
		if A[i]!=[]:
			return False		##demnach keine Eulertour vorhanden
			
	return blist
