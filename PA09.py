def quicksort(n,cmp,swp):					##Einzelne Funktion definieren, um Start und Endwert mit angeben zu können
	qs(0,n,cmp,swp)
	return 1

def qs(a,b,cmp,swp):
	if b-a == 2:							#Falls genau 2 Elemente sortiert werden sollen, nur diese beiden verlgeichen
		if cmp(a,a+1) is False:				#Falls nur ein Element sortiert werden soll, passiert nichts
			swp(a,a+1)
	elif b-a >= 3:							#Falls mehr als 2 Elemente sortiert werden sollen
		if cmp(a,a+1):						#PivotSuche
			if cmp(a+1,a+2):
				x=a+1
			else:
				if cmp(a,a+2):
					x=a+2
				else:
					x=a
		else:
			if not cmp(a+1,a+2):
				x=a+1
			else:
				if not cmp(a,a+2):
					x=a+2
				else:
					x=a
		swp(x,a)							#Setze Pivot an erste Stelle
		x=a
		for i in range(x+1,b):				#Vergleiche alle Elemente hinter Pivot, mit Pivot und tausche kleinere nach vorne
			if cmp(i,x) is True:
				for j in range(i,x,-1):
					swp(j,j-1)
				x+=1
		qs(a,x,cmp,swp)						#Sortiere alle Elemente vor Pivot
		qs(x+1,b,cmp,swp)					#Sortiere alle Elemente hinter Pivot 
	return 1
		
#def cmp(i,j):
	#return L[i]<=L[j]

#def swp(i,j):
	#global L
	#L[i],L[j]=L[j],L[i]
			
	
		
			
				
