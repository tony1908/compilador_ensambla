import os

r= open ("temporal2.txt", "r")
w=open ("final.lst", "w")
fuente=open("exemplo.asc", "r")   #para tomar el codigo fuente comentario


def Escribir(ident, modo, indice_memoria_h): #funcion para escribir en el archivo
	indice_memoria_h2=indice_memoria_h.upper()
	if ident==1: #si es modo inherente
		w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t\t: "+indice_memoria_h2+"\t"+modo[1]+"\n")
		print (`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t\t: "+indice_memoria_h2+"\t"+modo[1]+"\t")
	
	elif ident==2: #si es modo inmediato
		if len(ejemplo)==2:
			if len(ejemplo[1])==4: #si tiene operando de 8 bits
				w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[2:4]+"\n")
				print (`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[2:4])
			elif len(ejemplo[1])==6: #si tiene operando de 16 bits
				w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[2:6]+"\n")
				print(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[2:6])
		else:#si tiene una etiqueta
			if len(ejemplo[1])==4: #si tiene operando de 8 bits
				w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[2:4]+"\n")
				print (`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[2:4])
			elif len(ejemplo[1])==6: #si tiene operando de 16 bits
				w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[2:6]+"\n")
				print(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[2:6])
				
	elif ident==3: #si es modo extendido
		if len(ejemplo)==2:
			w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[1:6]+"\n") #aqui puede haber una condicion q marque error si el operador no es de 16 bits
			print(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[1:6])
		else:	#si tiene una etiqueta
			w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[1:6]+"\n") #aqui puede haber una condicion q marque error si el operador no es de 16 bits
			print(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[1:6])
	
	elif ident==4: #si es modo directo
		if len(ejemplo)==2:
			w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[1:4]+"\n") #la misma condicion de arriba pero con 8 bits
			print(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[1:4])
		else:#si tiene una etiqueta
			w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[1:4]+"\n") #la misma condicion de arriba pero con 8 bits
			print(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[1:4])
	
	elif ident==5: #si es modo indexado
		if len(ejemplo)==2:
			w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[1:3]+"\n")
			print (`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[1])[1:3])
		else:#si tiene una etiqueta
			w.write(`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[1:3]+"\n")
			print (`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+modo[1]+(ejemplo[2])[1:3])




def Dec_a_Hexa(dato):
	numero=dato
	numero2=hex(numero)
	return numero2[2:6]

def Hexa_a_Dec(dato):
	numero=dato
	aux=str(numero)
	numero2=int(aux,16)
	return numero2

def Calcula_Salto(numero1, numero2): 
	numero1=Hexa_a_Dec(numero1) #en el q estoy
	numero2=Hexa_a_Dec(numero2) #al q quiero saltar

	if numero2<numero1:
		resultado=numero1-numero2
		resultado=256-resultado
		return hex(resultado)[2:6]
	else:
		resultado=numero2-numero1
		return hex(resultado)[2:6]



lineas=r.readlines()
lineas_ejemplo=0
ident=0                        #identificador del modo de direccionamiento
indice_memoria=0
indice_memoria_aux=0         #auxiliar par el modo relativo
indice_memoria_h_aux=0     #auxiliar para el modo relativo
opcode=0					#auxiliar para el modo relativo


for j in lineas: #Conteo de lineas totales del archivo
	lineas_ejemplo=lineas_ejemplo+1
r.seek(0,0) #Coloca el puntero al inicio del archivo


for i in range(lineas_ejemplo):                      #empieza la lecutra linea por linea del archivo    
	ejemplo=(r.readline()).split()
	ejemplo_fuente=(fuente.readline()).split()


	if len(ejemplo)==0:  #para detectar renglones en blanco
		indice_memoria_h=Dec_a_Hexa(indice_memoria)
		indice_memoria_h2=indice_memoria_h.upper()
		print `i+1`+"\t\t\t\t: "+indice_memoria_h2
		w.write (`i+1`+"\t\t\t\t: "+indice_memoria_h2+"\n")


	elif (ejemplo_fuente[0])[:1]=='*' or ( len(ejemplo)==3 and (ejemplo_fuente[2])[:1]=='*'): #para detectar comentarios al principio
		indice_memoria_h=Dec_a_Hexa(indice_memoria)
		print `i+1`+"\t"+" ".join(ejemplo_fuente)
		w.write (`i+1`+"\t\n")


	elif len(ejemplo)==3 and ejemplo[1]=='EQU': #directiva EQU
		print `i+1`+"\t"+" ".join(ejemplo)+"\t\t: "+(ejemplo[2])[1:6]
		w.write (`i+1`+"\t"+"".join(ejemplo[0])+"\t\t: "+(ejemplo[2])[1:6]+"\n")

	
	elif (len(ejemplo)>1 and ejemplo[0]=='ORG'): #directiva ORG
		indice_memoria_h= ejemplo[1][1:5]#int(ejemplo[1][1:5])
		indice_memoria=Hexa_a_Dec(indice_memoria_h)
		indice_memoria_h=Dec_a_Hexa(indice_memoria)



	elif ejemplo[0]=='END': #directiva END
		indice_memoria_h=Dec_a_Hexa(indice_memoria)
		indice_memoria_h2=indice_memoria_h.upper()
		print `i+1`+"\t"+ejemplo[0]+"\t\t\t: "+indice_memoria_h2
		w.write (`i+1`+"\t"+ejemplo[0]+"\t\t\t: "+indice_memoria_h2+"\n")
		break


	elif len(ejemplo)>1 and ejemplo[0]=='FCB': #directiva FCB
		indice_memoria_h=Dec_a_Hexa(indice_memoria)
		indice_memoria_h2=indice_memoria_h.upper()
		print `i+1`+"\t"+" ". join (ejemplo)+"\t\t: "+indice_memoria_h2+"\t"+(ejemplo[1])[1:3]+(ejemplo[1])[5:7]
		w.write(`i+1`+"\t"+" ". join (ejemplo)+"\t\t: "+indice_memoria_h2+"\t"+(ejemplo[1])[1:3]+(ejemplo[1])[5:7]+"\n")

	elif len(ejemplo)>1 and ejemplo[1]=='FCB': #directiva FCB (cuando tiene una etiqueta antes)
		indice_memoria_h=Dec_a_Hexa(indice_memoria)
		indice_memoria_h2=indice_memoria_h.upper()
		print `i+1`+"\t"+" ". join (ejemplo)+"\t\t: "+indice_memoria_h2+"\t"+(ejemplo[2])[1:3]+(ejemplo[2])[5:7]
		w.write(`i+1`+"\t"+" ". join (ejemplo)+"\t\t: "+indice_memoria_h2+"\t"+(ejemplo[2])[1:3]+(ejemplo[2])[5:7]+"\n")


	elif ejemplo[0]=='BCC' or ejemplo[0]=='BCS' or ejemplo[0]=='BEQ' or ejemplo[0]=='BGE' or ejemplo[0]=='BGT' or ejemplo[0]=='BHI' or ejemplo[0]=='BHS' or ejemplo[0]=='BLE' or ejemplo[0]=='BLO' or ejemplo[0]=='BLS' or ejemplo[0]=='BLT' or ejemplo[0]=='BMI' or ejemplo[0]=='BNE' or ejemplo[0]=='BPL' or ejemplo[0]=='BRA' or ejemplo[0]=='BRN' or ejemplo[0]=='BSR' or ejemplo[0]=='BVC' or ejemplo[0]=='BVS':
		indice_memoria_aux=indice_memoria+2                        #todos los relativos usan 2 bytes
		indice_memoria_h_aux=Dec_a_Hexa(indice_memoria_aux)
		salto=Calcula_Salto(indice_memoria_h_aux, (ejemplo[1])[1:5])
		indice_memoria_h=Dec_a_Hexa(indice_memoria)
		indice_memoria_h2=indice_memoria_h.upper()

		if ejemplo[0]=='BCC':
			opcode='24'
		elif ejemplo[0]=='BCS':
			opcode='25'
		elif  ejemplo[0]=='BEQ':
			opcode='27'
		elif ejemplo[0]=='BGE':
			opcode='2C'
		elif ejemplo[0]=='BGT':
			opcode='2E'
		elif ejemplo[0]=='BHI':
			opcode='22'
		elif ejemplo[0]=='BHS':
			opcode='24'
		elif ejemplo[0]=='BLE':
			opcode='2F'
		elif ejemplo[0]=='BLO':
			opcode='25'
		elif ejemplo[0]=='BLS':
			opcode='23'
		elif ejemplo[0]=='BLT':
			opcode='2D'
		elif ejemplo[0]=='BMI':
			opcode='2B'
		elif ejemplo[0]=='BNE':
			opcode='26'
		elif ejemplo[0]=='BPL':
			opcode='2A'
		elif ejemplo[0]=='BRA':
			opcode='20'
		elif ejemplo[0]=='BRN':
			opcoce='21'
		elif ejemplo[0]=='BSR':
			opcode='8D'
		elif ejemplo[0]=='BVC':
			opcode='28'
		elif ejemplo[0]=='BVS':
			opcode='29'

		print `i+1`+"\t"+" ". join (ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+opcode+salto
		w.write (`i+1`+"\t"+" ". join (ejemplo_fuente)+"\t\t: "+indice_memoria_h2+"\t"+opcode+salto+"\n")
		indice_memoria=indice_memoria+2


	elif len(ejemplo)==1:
		if (ejemplo[0]=='ABA' or ejemplo[0]=='ABX' or ejemplo[0]=='ABY' or ejemplo[0]=='ASLA' or ejemplo[0]=='ASLB' or ejemplo[0]=='ASLD' or ejemplo[0]=='ASRA' or ejemplo[0]=='ASRB' or ejemplo[0]=='CBA' or ejemplo[0]=='CLC'):
			r1=open("inherente.txt", "r")
			modo=(r1.readline()).split()
			ident=1
			while ejemplo[0]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif (ejemplo[0]=='CLI' or ejemplo[0]=='CLRA' or ejemplo[0]=='CLRB' or ejemplo[0]=='CLV' or ejemplo[0]=='COMA' or ejemplo[0]=='COMB' or ejemplo[0]=='DAA' or ejemplo[0]=='DECA' or ejemplo[0]=='DECB' or ejemplo[0]=='DES' or ejemplo[0]=='DEX' or ejemplo[0]=='DEY' or ejemplo[0]=='FDIV' or ejemplo[0]=='IDIV' or ejemplo[0]=='INCA' or ejemplo[0]=='INCB' or ejemplo[0]=='INS' or ejemplo[0]=='INX' or ejemplo[0]=='INY'):
			r1=open("inherente.txt", "r")
			modo=(r1.readline()).split()
			ident=1
			if ejemplo[0]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif (ejemplo[0]=='LSLA' or ejemplo[0]=='LSLB' or ejemplo[0]=='LSLD' or ejemplo[0]=='LSRA' or ejemplo[0]=='LSRB' or ejemplo[0]=='LSRD' or ejemplo[0]=='MUL' or ejemplo[0]=='NEGA' or ejemplo[0]=='NEGB' or ejemplo[0]=='NOP' or ejemplo[0]=='PSHA' or ejemplo[0]=='PSHB' or ejemplo[0]=='PSHX' or ejemplo[0]=='PSHY' or ejemplo[0]=='PULA' or ejemplo[0]=='PULB' or ejemplo[0]=='PULX' or ejemplo[0]=='PULY' or ejemplo[0]=='ROLA' or ejemplo[0]=='ROLB' or ejemplo[0]=='RORA'):
			r1=open("inherente.txt", "r")
			modo=(r1.readline()).split()
			ident=1
			while ejemplo[0]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif (ejemplo[0]=='RORB' or ejemplo[0]=='RTS' or ejemplo[0]=='SBA'  or ejemplo[0]=='SEC'   or ejemplo[0]=='SEI'   or ejemplo[0]=='SEV'   or ejemplo[0]=='STOP'   or ejemplo[0]=='SWI'   or ejemplo[0]=='TAB'   or ejemplo[0]=='TAP'   or ejemplo[0]=='TBA'   or ejemplo[0]=='TETS'  or ejemplo[0]=='TPA'  or ejemplo[0]=='TSTA'   or ejemplo[0]=='TSTB'   or ejemplo[0]=='TSX'   or ejemplo[0]=='TSY'   or ejemplo[0]=='TXS'   or ejemplo[0]=='TYS'   or ejemplo[0]=='WAI'   or ejemplo[0]=='XGDX'   or ejemplo[0]=='XGDY' ):
			r1=open("inherente.txt", "r")
			modo=(r1.readline()).split()
			ident=1
			while ejemplo[0]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		else:
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			indice_memoria_h2=indice_memoria_h.upper()
			print `i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t\t: "+indice_memoria_h2
			w.write (`i+1`+"\t"+" ".join(ejemplo_fuente)+"\t\t\t: "+indice_memoria_h2+"\n")

	elif len(ejemplo)==2:
		if (ejemplo[1])[:1]=='#': #si el primer elemento es '#', es inmediato
			r1= open("inmediato.txt", "r")
			modo=(r1.readline()).split()
			ident=2
			while ejemplo[0]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif (len(ejemplo[1])>=4 and (ejemplo[1])[3:4]!=','): #si el operando es >= 4, tiene 16 bits, es extendido (lleva la condicion para no tomar los indexados)
			r1=open("extendido.txt","r")
			modo=(r1.readline()).split()
			ident=3
			while ejemplo[0]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif len(ejemplo[1])==3: 
			r1=open("directo.txt", "r")
			modo=(r1.readline()).split()
			ident=4
			if ejemplo[0]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif (ejemplo[1])[3:4]==',': 
			if (ejemplo[1])[4:5]=='X':
				r1=open("indexadox.txt", "r")
			else:
				r1=open("indexadoy.txt", "r")
			modo=(r1.readline()).split()
			ident=5
			while ejemplo[0]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])	
		else:
			r1=open("inherente.txt", "r")
			modo=(r1.readline()).split()
			ident=1
			while ejemplo[1]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])

	elif len(ejemplo)==3:
		if (ejemplo[2])[:1]=='#': #si el primer elemento es '#', es inmediato
			r1= open("inmediato.txt", "r")
			modo=(r1.readline()).split()
			ident=2
			while ejemplo[1]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif (len(ejemplo[2])>=4 and (ejemplo[2])[3:4]!=','): #si el operando es >= 4, tiene 16 bits, es extendido (lleva la condicion para no tomar los indexados)
			r1=open("extendido.txt","r")
			modo=(r1.readline()).split()
			ident=3
			while ejemplo[1]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif len(ejemplo[2])==3: 
			r1=open("directo.txt", "r")
			modo=(r1.readline()).split()
			ident=4
			if ejemplo[1]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])
		elif (ejemplo[2])[3:4]==',': 
			if (ejemplo[2])[4:5]=='X':
				r1=open("indexadox.txt", "r")
			else:
				r1=open("indexadoy.txt", "r")
			modo=(r1.readline()).split()
			ident=5
			while ejemplo[1]!=modo[0]:
				modo=(r1.readline()).split()
			indice_memoria_h=Dec_a_Hexa(indice_memoria)
			Escribir(ident, modo, indice_memoria_h)
			indice_memoria=indice_memoria+int(modo[2])


w.close()
r.close()



#os.remove('temporal.txt')
#os.remove('temporal2.txt')





