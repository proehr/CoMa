def auswertung(wort, interpretation):
	if len(wort)==0:
		return (True, 0)
	a=[]
	while len(wort)>0:
		if wort[0]=="x" and len(wort)>1:
			p=0
			while not (wort[p+1]=="(" or wort[p+1]==")" or wort[p+1]=="[" or wort[p+1]=="]" or wort[p+1]=="&" or wort[p+1]=="|" or wort[p+1]=="!"):
				p=p+1
				if p==len(wort)-1:
					break

			l=""
			for i in range(p+1):
				l=l+wort[i]	
			a.append(l)
			wort=wort[p+1:]
		else:
			a.append(wort[0])
			wort=wort[1:]																													#Splitte wort in möglichst sinnvolle Komponenten auf
	for i in range(len(a)):
		for k in range(len(interpretation)):
			if a[i]=="x"+str(k):
				a[i]=str(interpretation[k])
		if a[i]=="|":
			a[i]="or"	
		elif a[i]=="&":
			a[i]="and"	
		elif a[i]=="!":
			a[i]="not"	
		elif a[i]=="(":
			a[i]="("	
		elif a[i]==")":
			a[i]=")"
		elif a[i]=="[":
			a[i]="["	
		elif a[i]=="]":
			a[i]="]"
		elif a[i]=="True" or a[i]=="False":
			a[i]=a[i]				
		else:
			raise Exception('Fehlermeldung')																								#Benenne die Komponenten um, falls sie sinnvoll sind, andernfalls raise Exception
				
	x=0
	y=0
	for i in range(len(a)):
		if a[i]=="(":
			x+=1
		elif a[i]==")":
			x-=1
		elif a[i]=="[":
			y+=1
		elif a[i]=="]":
			y-=1
	if x!=0 or y!=0:
		raise Exception('Fehlermeldung')																									#Zählung, bei ungleicher Anzahl öffnender und schließender Klammern raise Exception
	
	string=""
	for i in range(len(a)):
		if a[i]=="[":
			string=string+"("+" "
		elif a[i]=="]":
			string=string+")"+" "
		else:
			string=string+a[i]+" "
	string=string[:-1]																														#Alles in einen String	
	
	k=[0]																																	#Klammertiefe zählen
	s=[]																																	#Prüfen, ob Klammerungen stimmen, also dass es keine nichttrivialen Schnitte gibt 
	index=[]																																#Prüfen, ob Wahrheitswert zwischen Klammern steht
	q=0
	b=a
	while q <len(b):
		if b[q]=="(" or b[q]=="[":	
			s.append(b[q])
			k[-1]=k[-1]+1
			b[q]="_"
			index.append(q)
			break
		else:
			q+=1	
	if len(s)>0:
		for i in range(q):
			if b[i]==")" or b[i]=="]":
				raise Exception("Fehlermeldung")
					
		for i in range(len(b)):	
			if b[i]=="(" or b[i]=="[":	
				s.append(b[i])
				b[i]="_"	
				k[-1]=k[-1]+1
				index.append(i)				
			elif b[i]==")" and s[-1]=="(":
				s.pop()
				b[i]="_"
				k.append(k[-1]-1)
				p=index[-1]
				while p <i:
					if b[p]=="True" or b[p]=="False":
						break
					else:
						p+=1
				if p==i:
					raise Exception("Fehlermeldung")		 	
			elif b[i]=="]" and s[-1]=="[":
				s.pop()
				b[i]="_"	
				k.append(k[-1]-1)
				p=index[-1]
				while p <i:
					if b[p]=="True" or b[p]=="False":
						break
					else:
						p+=1
				if p==i:
					raise Exception("Fehlermeldung")
			elif b[i]=="]" and not s[-1]=="[":
				raise Exception("Fehlermeldung")
			elif b[i]==")" and not s[-1]=="(":
				raise Exception("Fehlermeldung")					
	if len(s)>0:
		raise Exception("Fehlermeldung")


	for i in range(len(a)-1):												#Fehlerbehebung - was tun bei falscher Eingabe
		if a[i]=="not" or a[i]=="or" or a[i]=="and":
			if a[i+1]==")" or a[i+1]=="]":
				raise Exception("Fehlermeldung")
			else: 
				z=i+1
				while z<len(a):
					if a[z]=="True" or a[z]=="False":
						break
					else:
						z+=1		
				if z==len(a):
					raise Exception("Fehlermeldung")
				else:
					for p in range(i+1,z):
						if a[p]=="or" or a[p]=="and":
							raise Exception("Or-and,And-and,Not-or,...")			 
		elif a[i]=="True" or a[i]=="False":
			z=i+1
			while z<len(a):
				if a[z]=="True" or a[z]=="False":
						break
				else:
					z+=1
			if z!=len(a):
				tester=False
				for l in range(i+1,z):
					if a[l]=="or" or a[l]=="and":
						tester=True
						break
				if tester==False:
					raise Exception("Fehlende Verknuepfung von Wahrheitswerten.")


			
	if a[-1]=="not" or a[-1]=="or" or a[-1]=="and":
		raise Exception("Fehlermeldung")	


	boolean=eval(string)
	klammertiefe=max(k)
#	klammertiefe=0			
#	for i in range(len(a)):
#		if a[i]=="(" or a[i]=="[":
#			klammertiefe+=1
	return (bool(boolean), int(klammertiefe))		

def test():
	print(auswertung("!!x0|x1&x2", [True, True, False]))
	print(auswertung("(!!x0|x1)&x2", [True, True, False]))
	print(auswertung("!([!x0]|[[x1]&x2])", [True, True, False]))
	print(auswertung("x0|!x0", [True]))
	print(auswertung("x0x1", [True, True]))
	print(auswertung("(x0|x1]", [False, False]))
	print(auswertung("(x0|x1", [True, False]))
	print(auswertung("x0!|x1", [True, False]))


#Aufgaben: Klammertiefe wird bisher falsch gezählt, Prüfe ob Klammern richtig öffnen, schließen
