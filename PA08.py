def ungeklammert(ohnek):
	y=ohnek
	if len(ohnek)==0:
		raise Exception('in einer Klammer muss etwas stehen')
	while "!" in ohnek:
		a=ohnek.index("!")
		if a==len(ohnek)-1:
			raise Exception('Auf ! muss eine Variable folgen')
		elif ohnek[a+1]=="w":
			ohnek=ohnek[:a]+"f"+ohnek[a+2:]
		elif ohnek[a+1]=="f":
			ohnek=ohnek[:a]+"w"+ohnek[a+2:]
		else:
			raise Exception('Auf ! muss eine Variable folgen')
			
	while "&" in ohnek:
		a=ohnek.index("&")
		if a==len(ohnek)-1 or a==0:
			raise Exception('& wurde nicht korrekt verwendet')
		elif ohnek[a-1]=="w" and ohnek[a+1]=="w":
			ohnek=ohnek[:a-1]+"w"+ohnek[a+2:]
		else:
			ohnek=ohnek[:a-1]+"f"+ohnek[a+2:]
			
	while "|" in ohnek:
		a=ohnek.index("|")
		if a==len(ohnek)-1 or a==0:
			raise Exception('| wurde nicht korrekt verwendet')
		elif ohnek[a-1]=="w" or ohnek[a+1]=="w":
			ohnek=ohnek[:a-1]+"w"+ohnek[a+2:]
		else:
			ohnek=ohnek[:a-1]+"f"+ohnek[a+2:]
			
	if len(ohnek)>1:
		raise Exception(y + ' ist kein gültiger Ausdruck')
		
	return ohnek
	
def auswertung(wort, interpretation):
	if len(wort)<1:
		return(True,0)
	for i in range(len(interpretation)-1,-1,-1):
		if interpretation[i] is True:
			wort=wort.replace("x"+str(i),"w")
		elif interpretation[i] is False:
			wort=wort.replace("x"+str(i),"f")
			
	if "!!" in wort:
		wort=wort.replace("!!","")
		
	if " " in wort:
		wort=wort.replace(" ","")
		
	if "&&" in wort or "&|" in wort or "|&" in wort or "||" in wort:
		raise Exception(wort + ' ist keine gültige Aussage')
		
	b=""
	St=[["",""]]
	d=len(St)	
	for i in range(len(wort)):
		if wort[i]=="(":
			St.append([")",b])
			b=""
			if len(St)>d:
				d=len(St)
		elif wort[i]=="[":
			St.append(["]",b])
			b=""
			if len(St)>d:
				d=len(St)
		elif wort[i]==")" or wort[i]=="]":
			if St[-1][0]!=wort[i]:
				raise Exception('Klammern passen nicht zusammen')
			else:
				b=St[-1][1]+ungeklammert(b)
				St=St[:-1]
		else: 
			b=b+wort[i]
		
			
	d-=1
				
	if len(St)>1:
		raise Exception('Klammer wird nicht geschlossen')
		
	b=ungeklammert(b)
	
	if b=="w":
		return(True,d)
	elif b=="f":
		return(False,d)
	else:
		raise Exception(wort + ' ist kein gültiger Ausdruck')
	
	
			
