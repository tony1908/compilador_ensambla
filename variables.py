def Elim_Com(prueba):
	aux=len(prueba)
	for j in range(len(prueba)):
		if '*' in prueba[j] :
			aux=j
	for k in range(aux, len(prueba)):
		prueba.pop()
	return prueba

def ASCII(caracter):
	CR7=open("ASCII.txt", "r")
	lineas=CR7.readlines()
	lineas_ej=0

	for j in lineas:               #conteo de lineas
		lineas_ej=lineas_ej+1
	CR7.seek(0,0)

	compa=(CR7.readline()).split()
	for i in range(lineas_ej):  #busqueda del caracter
		while compa[0]!=caracter:
			compa=(CR7.readline()).split()

	CR7.seek(0,0)
	return compa[1]





r= open ("exemplo.asc", "r")
w=open ("temporal.txt", "w")

lineas=r.readlines()
lineas_ejemplo=0

variables={}     # diccionario para variables declaradas con EQU

for j in lineas: #Conteo de lineas totales del archivo
	lineas_ejemplo=lineas_ejemplo+1
r.seek(0,0) #Coloca el puntero al inicio del archivo


for i in range(lineas_ejemplo):           #llenado del diccionario de variables declaradas con directiva EQU
	ejemplo1=(r.readline()).split()
	if (len(ejemplo1)>1 and ejemplo1[1]=='EQU'):
		variables[ejemplo1[0]]=ejemplo1[2]
	#print variables
r.seek(0,0)


for j in range(lineas_ejemplo):
	ejemplo=(r.readline()).split()

	if len(ejemplo)==0:  #para detectar renglones en blanco
		w.write("\n")
	
	elif len(ejemplo)==1:
		w.write(" ".join(ejemplo)+"\n")
	
	elif len(ejemplo)>1 and (ejemplo[0])[0:1]=='*':  #identifica las lineas q inician con comentario para dejarlas en el archivo temporal
		w.write(" ".join(ejemplo)+"\n")

	
	elif len(ejemplo)>1:
		if len(ejemplo[1])==3 and (ejemplo[1])[1:2]=="'":    #cambio de variables a ASCII
			aux=ASCII((ejemplo[1])[2:3])
			ejemplo[1]="#$"+aux
			w.write(" ".join(ejemplo)+"\n")

		elif len(ejemplo)==3 and len(ejemplo[2])==3 and (ejemplo[2])[1:2]=="'":         #cambio de variables a ASCII
			aux=ASCII((ejemplo[2])[2:3])
			ejemplo[2]="#$"+aux
			w.write(" ".join(ejemplo)+"\n")

		else:
			linea_aux=Elim_Com(ejemplo)
			for k in range (len(variables)):
			 	if  len(linea_aux)>1  :
		 			if (variables.keys())[k] in linea_aux[1] and (linea_aux[1])[0:1]=='#':
			 			linea_aux[1]="#"+variables[(variables.keys())[k]]
		 			elif len(linea_aux)==3 and (variables.keys())[k] in linea_aux[2]:
			 			linea_aux[2]=variables[(variables.keys())[k]]
		 			elif len(linea_aux)==2 and (variables.keys())[k] in linea_aux[1]:
			 			linea_aux[1]=variables[(variables.keys())[k]]

		 			
			w.write(" ".join(linea_aux)+"\n")

	



w.close()
r.close()