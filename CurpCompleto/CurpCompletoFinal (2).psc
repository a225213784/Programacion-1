//Nombre del archivo: Tarea 3: ¿Tu sabes la clave?
//Autores: Cristobal Ochoa y Christian Alexandro Lopez (Grupo1)
//Fecha: 11/10/2026
//Descripción: Programa que una vez se insertan los datos personales de un individuo, con base en estos, procesa y formula el curp de este mismo 


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función que gestionará los primeros 4 digitos de la curp.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion prim4dig <- Gestionadorprim4dig(nombre,apellidoM,apellidoP)
	Definir primdig,segdig, terdig, cuadig,nomaux,aux1,aux2,prim4dig Como Caracter
	Definir nomespecial,apellidoespecial Como Logico
	Definir numaux, compuestoN, compuestoP, compuestoM,longN,longP,longM Como Entero
	
	
	compuestoP <- VerificadorCompuesto(apellidoP)
	longP <- Longitud(apellidoP)
	apellidoP <- Minusculas(apellidoP)
	Si compuestoP <> 0  Entonces
		numaux <- compuestoP - 1
		nomaux <- Subcadena(apellidoP, 0,numaux) 
		Si  nomaux = 'da' o nomaux = 'das' o nomaux = 'de' o nomaux = 'del' o nomaux = 'der' o nomaux = 'di' o nomaux = 'dd' o nomaux = 'el' o nomaux = 'la' o nomaux = 'los' o nomaux = 'las' o nomaux = 'le' o nomaux = 'les' o nomaux = 'mac' o nomaux = 'mc' o nomaux = 'von' o  nomaux = 'van' o nomaux = 'y' Entonces
			numaux <- compuestoP + 1
			apellidoP <- Subcadena(apellidoP, numaux,longP)
		FinSi
	FinSi
	
	//Revisará si el contenido del digito 1 es inválido y entonces lo reemplazará por una X
	primdig <- Obtenerprimdig(apellidoP)
	Si primdig = '.' o primdig = '-' o primdig = '/' o primdig = 'ñ' Entonces
		primdig <- 'x' 
	FinSi
	
	//Revisará si el contenido del digito 2 es inválido y entonces lo reemplazará por una X
	segdig <- Obtenerprimvocint(apellidoP)
	Si segdig = '' Entonces
		segdig <- 'x'
	FinSi
	
	apellidoM <- Minusculas(apellidoM)
	Si apellidoM = 'xxx' Entonces
		apellidoM <- 'x' 
	FinSi
	
	//Revisará si el contenido del digito 3 es inválido y entonces lo reemplazará por una X
	terdig <-  Obtenerprimdig(apellidoM)
	Si terdig = '' o terdig = 'ñ' Entonces
		terdig <- 'x'
	FinSi
	
	//Verificación de si el nombre es un caso de excepción
	compuestoN <- VerificadorCompuesto(nombre)
	nombre <- Minusculas(nombre) 
	longN <- Longitud(nombre)
	Si compuestoN <> 0  Entonces
		numaux <- compuestoN - 1
		nomaux <- Subcadena(nombre, 0,numaux) 
		Si  nomaux = 'maria' o nomaux = 'ma.' o nomaux = 'ma' o nomaux = 'jose' o nomaux = 'j.' o nomaux = 'j' o nomaux = 'da' o nomaux = 'das' o nomaux = 'de' o nomaux = 'del' o nomaux = 'der' o nomaux = 'di' o nomaux = 'dd' o nomaux = 'el' o nomaux = 'la' o nomaux = 'los' o nomaux = 'las' o nomaux = 'le' o nomaux = 'les' o nomaux = 'mac' o nomaux = 'mc' o nomaux = 'von' o  nomaux = 'van' o nomaux = 'y' Entonces
			numaux <- compuestoN + 1
			nombre <- Subcadena(nombre, numaux,longN)
		FinSi
	FinSi
	
	//Revisará si el contenido del digito 4 es inválido y entonces lo reemplazará por una X
	cuadig <- Obtenerprimdig(nombre) 
	Si cuadig = '.' o cuadig = '-' o cuadig = '/' o cuadig = 'ñ' Entonces
		cuadig <- 'x' 
	FinSi
	
	 //Unión de los digitos para formar los primero 4 digitos y comprobación de que al juntar los digitos el resultado no sea una combinación mal sonante.
	aux1 <- Concatenar(primdig,segdig)
	aux2 <- Concatenar(terdig,cuadig)
	prim4dig <- Concatenar(aux1,aux2)
	prim4dig <- ComprobadorMalSonante(prim4dig)
	
FinFuncion

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para arreglar los primeros 4 digitos si el resultado de ellos es una palabra mal sonante.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion prim4digV <- ComprobadorMalSonante(prim4dig)
	Definir prim4digV Como Caracter
	prim4dig <- Mayusculas(prim4dig)
	prim4digV <- prim4dig
	
	
	Segun prim4dig Hacer
		'BACA':
			prim4digV <- 'BXCA'
		'BAKA':
			prim4digV <- 'BXKA'
		'BUEI':
			prim4digV <- 'BXEI'
		'BUEY':
			prim4digV <- 'BXEY'
		'CACA':
			prim4digV <- 'CXCA'
		'CACO':
			prim4digV <- 'CXCO'
		'CAGA':
			prim4digV <- 'CXGA'
		'CAGO':
			prim4digV <- 'CXGO'
		'CAKA':
			prim4digV <- 'CXKA'
		'CAKO':
			prim4digV <- 'CXKO'
		'COGE':
			prim4digV <- 'CXGE'
		'COGI':
			prim4digV <- 'CXGI'
		'COJA':
			prim4digV <- 'CXJA'
		'COJE':
			prim4digV <- 'CXJE'
		'COJI':
			prim4digV <- 'CXJI'
		'COJO':
			prim4digV <- 'CXJO'
		'COLA':
			prim4digV <- 'CXLA'
		'CULO':
			prim4digV <- 'CXLO'
		'FALO':
			prim4digV <- 'FXLO'
		'FETO':
			prim4digV <- 'FXTO'
		'GETA':
			prim4digV <- 'GXTA'
		'GUEI':
			prim4digV <- 'GXEI'
		'GUEY':
			prim4digV <- 'GXEY'
		'JETA':
			prim4digV <- 'JXTA'
		'JOTO':
			prim4digV <- 'JXTO'
		'KACA':
			prim4digV <- 'KXCA'
		'KACO':
			prim4digV <- 'KXCO'
		'KAGA':
			prim4digV <- 'KXGA'
		'KAGO':
			prim4digV <- 'KXGO'
		'KAKA':
			prim4digV <- 'KXKA'
		'KAKO':
			prim4digV <- 'KXKO'
		'KOGE':
			prim4digV <- 'KXGE'
		'KOGI':
			prim4digV <- 'KXGI'
		'KOJA':
			prim4digV <- 'KXJA'
		'KOJE':
			prim4digV <- 'KXJE'
		'KOJI':
			prim4digV <- 'KXJI'
		'KOJO':
			prim4digV <- 'KXJO'
		'KOLA':
			prim4digV <- 'KXLA'
		'KULO':
			prim4digV <- 'KXLO'
		'LILO':
			prim4digV <- 'LXLO'
		'LOCA':
			prim4digV <- 'LXCA'
		'LOCO':
			prim4digV <- 'LXCO'
		'LOKA':
			prim4digV <- 'LXKA'
		'LOKO':
			prim4digV <- 'LXKO'
		'MAME':
			prim4digV <- 'MXME'
		'MAMO':
			prim4digV <- 'MXMO'
		'MEAR':
			prim4digV <- 'MXAR'
		'MEAS':
			prim4digV <- 'MXAS'
		'MEON':
			prim4digV <- 'MXON'
		'MIAR':
			prim4digV <- 'MXAR'
		'MION':
			prim4digV <- 'MXON'
		'MOCO':
			prim4digV <- 'MXCO'
		'MOKO':
			prim4digV <- 'MXKO'
		'MULA':
			prim4digV <- 'MXLA'
		'MULO':
			prim4digV <- 'MXLO'
		'NACA':
			prim4digV <- 'NXCA'
		'NACO':
			prim4digV <- 'NXCO'
		'PEDA':
			prim4digV <- 'PXDA'
		'PEDO':
			prim4digV <- 'PXDO'
		'PENE':
			prim4digV <- 'PXNE'
		'PIPI':
			prim4digV <- 'PXPI'
		'PITO':
			prim4digV <- 'PXTO'
		'POPO':
			prim4digV <- 'PXPO'
		'PUTA':
			prim4digV <- 'PXTA'
		'PUTO':
			prim4digV <- 'PXTO'
		'QULO':
			prim4digV <- 'QXLO'
		'RATA':
			prim4digV <- 'RXTA'
		'ROBA':
			prim4digV <- 'RXBA'
		'ROBE':
			prim4digV <- 'RXBE'
		'ROBO':
			prim4digV <- 'RXBO'
		'RUIN':
			prim4digV <- 'RXIN'
		'SENO':
			prim4digV <- 'SXNO'
		'TETA':
			prim4digV <- 'TXTA'
		'VACA':
			prim4digV <- 'VXCA'
		'VAGA':
			prim4digV <- 'VXGA'
		'VAGO':
			prim4digV <- 'VXGO'
		'VAKA':
			prim4digV <- 'VXKA'
		'VUEI':
			prim4digV <- 'VXEI'
		'VUEY':
			prim4digV <- 'VXEY'
		'WUEI':
			prim4digV <- 'WXEI'
		'WUEY':
			prim4digV <- 'WXEY'
			
	FinSegun
	
FinFuncion


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Subproceso para verificar el usuario haya ingresado un nombre y no haya dejado vacio
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Subproceso VerificadorNombres(texto1 Por Referencia)
	Definir long Como Entero
	long <- Longitud(texto1) 
	Mientras long = 0 Hacer
		Escribir 'Dato inválido, favor de reinsertar'
		leer texto1 
		long <- Longitud(texto1)
	FinMientras
FinSubProceso

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función verificadora del compuesto
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Subproceso compuesto <- VerificadorCompuesto(texto1)
	Definir logaux Como Logico
	Definir long,i,compuesto  Como Entero
	Definir cadaux Como Caracter
	
	logaux <- Falso
	i <- 1
	long <- Longitud(texto1)
	compuesto <- 0
	Mientras i <= long y logaux = Falso  hacer 
		
		cadaux <- Subcadena(texto1, i,i)
		Si cadaux = ' ' Entonces
			compuesto <- i
			logaux <- Verdadero
		FinSi
		i <- i + 1 
	FinMientras
	
	Si compuesto - long =  0 Entonces
		compuesto <- 0 
	FinSi
	Si compuesto = 1 Entonces
		compuesto <- 0
	FinSi
	
FinSubProceso

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para obtener el primer digito
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion primdig <- Obtenerprimdig(texto1)
	Definir primdig Como Caracter
	primdig <- Subcadena(texto1,1,1) 
FinFuncion


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para obtener la primera vocal interna del apellido paterno
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion primvocint <- Obtenerprimvocint(texto1)
	Definir primvocint,cadaux  Como Caracter
	Definir i,long Como Entero
	Definir vocint Como Logico
	
	long <- Longitud(texto1)
	i <- 2
	vocint <- Falso
	
	primvocint <- ''
	
	Mientras i <= long y vocint = Falso Hacer
		cadaux <- Subcadena(texto1, i,i) 
		Si cadaux = 'a' o cadaux = 'e' o cadaux = 'i' o cadaux = 'o' o cadaux= 'u' o cadaux= 'ü' o cadaux='é' o cadaux='á' o cadaux='í' o cadaux='ó' o cadaux='ú' Entonces
			primvocint <- cadaux
			vocint <- Verdadero
		FinSi
		i <- i + 1 
	FinMientras
	
	Si primvocint <> '' Entonces
		Segun primvocint Hacer
			'á': 
				primvocint <- 'a'
			'é':
				primvocint <- 'e'
			'í': 
				primvocint <- 'i'
			'ó':
				primvocint <- 'o'
			'ú':
				primvocint <- 'u'
			'ü':
				primvocint <- 'u'
				
		FinSegun
	FinSi
	
FinFuncion

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para gestionar los digitos del  5  al 10 y unirlas para tener una variable con los digitos del 5 al 10
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion dig5_10 <- Gestionadordig5_10(fecha)
	Definir quindig,sexdig,sepdig,octdig,novdig,decdig,dig5_10,aux1,aux2,aux3,aux4 Como Caracter 
	
	quindig <- Subcadena(fecha, 9,9)
	sexdig <- Subcadena(fecha, 10,10)
	sepdig <- Subcadena(fecha, 4,4)
	octdig <- Subcadena(fecha, 5,5)
	novdig <- Subcadena(fecha, 1,1)
	decdig <- Subcadena(fecha, 2,2)
	
	aux1 <- Concatenar(quindig,sexdig)
	aux2 <- Concatenar(sepdig,octdig)
	aux3 <- Concatenar(novdig,decdig)
	aux4 <- Concatenar(aux1,aux2)
	
	dig5_10 <- Concatenar(aux4,aux3)
	
FinFuncion





///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para verificar que la fecha de nacimiento que haya ingresado el usuario sea correcta (Cumpla con el formato DD/MM/AAAA que en total da 10 digitos de longitud) y al verificar separa el dia, el mes y el año.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion ValFecha <- VerificacionFecha(fecha) 
	Definir long,dia,mes,ano Como Entero
	Definir ValFecha,auxb Como Logico
	Definir auxD,auxM,auxA,auxT,auxT1 Como Caracter
	long <- Longitud(fecha)
	
	ValFecha <- Verdadero
	
	auxT <- Subcadena(fecha, 3,3) 
	auxT1 <- Subcadena(fecha, 7,7)
	
	si auxT <> '/' y auxT1 <> '/' Entonces
		ValFecha <- Falso
	FinSi
	
	Si  long <> 10 Entonces
		ValFecha <- Falso
	SiNo
		auxd <- Subcadena(fecha, 0,2)
		auxM <- Subcadena(fecha, 4,5)
		auxA <- Subcadena(fecha, 7,10) 
		
		dia <- ConvertirANumero(auxD)
		mes <- ConvertirANumero(auxM)
		ano <- ConvertirANumero(auxA)
		auxb <- Gestionbisiesto(ano)
		
		Si mes >= 13 o mes <= 0 Entonces
			ValFecha <- Falso
		SiNo
			
			Segun mes Hacer
				1: 
					Si dia > 31 o dia <0 Entonces
						ValFecha <- Falso
					FinSi
				2:
					Si dia > 29 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
					
					Si dia = 29 y auxb = Falso Entonces
						ValFecha <- Falso
					FinSi
				3:
					Si dia > 31 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				4:
					Si dia > 30 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				5:
					Si dia > 31 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				6:
					Si dia > 30 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				7:
					Si dia > 31 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				8:
					Si dia > 31 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				9:
					Si dia > 30 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				10:
					Si dia > 31 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				11:
					Si dia > 30 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
				12:
					Si dia > 31 o dia < 0 Entonces
						ValFecha <- Falso
					FinSi
			FinSegun
		FinSi
		Si dia = 0 Entonces
			ValFecha <- Falso
		FinSi
	FinSi
	
	
FinSubProceso



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para comprobar si el año de nacimiento es bisiesto
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion anBis <- Gestionbisiesto(ano)
	Definir anBis Como Logico
	
	anbis <- Falso 
	Si ano%4 = 0 Entonces
		anBis<-Verdadero
		Si ano%100 = 0 Entonces
			anBis<-Falso 
			Si ano%400 = 0 Entonces
				anBis <- Verdadero
			FinSi
		FinSi
	FinSi
FinFuncion


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para gestionar el digito 11
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion oncdig <- Gestionadordig11(sexo)
	Definir oncdig Como Caracter
	oncdig<-sexo
FinFuncion

SubProceso VerificadorSexo(sexo Por Referencia)
	sexo <- Mayusculas(sexo)
	
	Mientras sexo <> 'H' y sexo <> 'M' Hacer
		Escribir 'Dato inválido, favor de reinsertar: ' Sin Saltar
		leer sexo
		sexo <- Mayusculas(sexo)
	FinMientras
FinSubProceso



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para verificar que el usuario no haya ingresado una opción de estado invalida
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
SubProceso VerificadorEstado(estado Por Referencia)
	
	Mientras estado > 33 o estado <= 0 Hacer
		Escribir 'Dato inválido, favor de reinsertar: ' Sin Saltar
		leer estado
		
	FinMientras
FinSubProceso


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para gestionar los digitos 12 y 13 (Estado)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion dig12_13 <- Gestionadordig12_13(estado)
	Definir dig12_13 Como Caracter
	
	Segun estado Hacer
		1:
			dig12_13 <- 'AS'
		2:
			dig12_13 <- 'BC'
		3:
			dig12_13 <- 'BS'
		4:
			dig12_13 <- 'CC'
		5:
			dig12_13 <- 'CL'
		6:
			dig12_13 <- 'CM'
		7:
			dig12_13 <- 'CS'
		8:
			dig12_13 <- 'CH'
		9:
			dig12_13 <- 'DF'
		10:
			dig12_13 <- 'DH'
		11:
			dig12_13 <- 'GT'
		12:
			dig12_13 <- 'GR'
		13:
			dig12_13 <- 'HG'
		14:
			dig12_13 <- 'JC'
		15:
			dig12_13 <- 'MC'
		16:
			dig12_13 <- 'MN'
		17:
			dig12_13 <- 'MS'
		18:
			dig12_13 <- 'NT'
		19:
			dig12_13 <- 'NL'
		20:
			dig12_13 <- 'OC'
		21:
			dig12_13 <- 'PL'
		22:
			dig12_13 <- 'QT'
		23:
			dig12_13 <- 'QR'
		24:
			dig12_13 <- 'SP'
		25:
			dig12_13 <- 'SL'
		26:
			dig12_13 <- 'SR'
		27:
			dig12_13 <- 'TC'
		28:
			dig12_13 <- 'TS'
		29:
			dig12_13 <- 'TL'
		30:
			dig12_13 <- 'VZ'
		31:
			dig12_13 <- 'YN'
		32:
			dig12_13 <- 'ZS'
		33:
			dig12_13 <- 'NE'
	FinSegun
FinFuncion



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para gestionar los digitos 14 al 16 y verificar que las consonantes internas sean invalida y en dado caso de que no se reemplazaran por X y al final unir los digitos.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion dig14_16 <- Gestionadordig14_16(nombre, apellidoM, apellidoP)
	Definir dig14,dig15,dig16,nomaux,nomespecial,aux1,dig14_16 Como Caracter
	Definir numaux, compuestoN,longN Como Entero
	
	apellidoP <- Minusculas(apellidoP)
	dig14 <- EncontrarConsint(apellidoP)
	
	Si dig14 = '' o dig14 = 'ñ' Entonces
		dig14 <- 'x'
	FinSi
	
	apellidoM <- Minusculas(apellidoM)
	dig15 <- EncontrarConsint(apellidoM)
	
	Si dig15 = 'xxx' Entonces
		dig15 <- 'x'
	FinSi
	
	Si dig15 = '' o dig15 = 'ñ' Entonces
		dig15 <- 'x'
	FinSi
	
	compuestoN <- VerificadorCompuesto(nombre)
	nombre <- Minusculas(nombre) 
	longN <- Longitud(nombre)
	Si compuestoN <> 0  Entonces
		numaux <- compuestoN - 1
		nomaux <- Subcadena(nombre, 0,numaux) 
		Si  nomaux = 'maria' o nomaux = 'ma.' o nomaux = 'ma' o nomaux = 'jose' o nomaux = 'j.' o nomaux = 'j' o nomaux = 'da' o nomaux = 'das' o nomaux = 'de' o nomaux = 'del' o nomaux = 'der' o nomaux = 'di' o nomaux = 'dd' o nomaux = 'el' o nomaux = 'la' o nomaux = 'los' o nomaux = 'las' o nomaux = 'le' o nomaux = 'les' o nomaux = 'mac' o nomaux = 'mc' o nomaux = 'von' o  nomaux = 'van' o nomaux = 'y' Entonces
			numaux <- compuestoN + 1
			nombre <- Subcadena(nombre, numaux,longN)
		FinSi
	FinSi
	
	dig16<- Encontrarconsint(nombre)
	
	Si dig16 = '' o dig16 = 'ñ' Entonces
		dig16 <- 'x'
	FinSi
	
	aux1 <- Concatenar(dig14,dig15)
	dig14_16 <- Concatenar(aux1,dig16)
	dig14_16 <- Mayusculas(dig14_16)
	
FinFuncion


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para obtener la primera consonante interna
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion primconsint <- EncontrarConsint(texto1) 
	Definir primconsint,cadaux  Como Caracter
	Definir i,long Como Entero
	Definir consint Como Logico
	long <- Longitud(texto1)
	i <- 2
	consint <- Falso
	Mientras i <= long y consint = Falso Hacer
		
		cadaux <- Subcadena(texto1, i,i) 
		Si cadaux = 'b' o cadaux = 'c' o cadaux = 'd' o cadaux = 'f' o cadaux= 'g' o cadaux= 'h' o cadaux='p' o cadaux='j' o cadaux='k' o cadaux='l' o cadaux='m' o cadaux='n' o cadaux='q' o cadaux='ñ' o cadaux='r' o cadaux='s' o cadaux='t' o cadaux='v'o cadaux='w' o cadaux='x' o cadaux='y' o cadaux='z' Entonces
			primconsint <- cadaux
			consint <- Verdadero
		FinSi
		i <- i + 1 
	FinMientras
FinFuncion


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Función para obtener la curp completa mediante los digitos ya obtenidos.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Funcion curpcomp <- ObtencionCurpComp(nombre,apellidoM,apellidoP,fecha,sexo,estado)
	Definir curpcomp,prim4dig,dig5_10,dig11,dig12_13,dig14_16,aux1,aux2,aux3 Como Caracter
	prim4dig <- Gestionadorprim4dig(nombre,apellidoM,apellidoP)
	dig5_10 <- Gestionadordig5_10(fecha)
	dig11 <- Gestionadordig11(sexo)
	dig12_13 <- Gestionadordig12_13(estado)
	dig14_16 <- Gestionadordig14_16(nombre, apellidoM, apellidoP)
	
	aux1 <- Concatenar(prim4dig,dig5_10)
	aux2 <- Concatenar(dig11,dig12_13)
	aux3 <- Concatenar(aux1,aux2)
	curpcomp <- Concatenar(aux3,dig14_16)
FinFuncion



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Proceso Principal
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Proceso CurpCompleto 
	Definir nombre,apellidoP,apellidoM,fecha,sexo,aux Como Caracter
	Definir prim4dig,estado   Como Entero
	Definir ValFecha Como Logico
	
	Escribir 'Favor de insertar los siguientes campos, en caso de no contar con uno de ellos inserte tres x ( xxx o XXX)'
	
	Escribir 'Nombre(s): '  Sin Saltar
	leer nombre 
	VerificadorNombres(nombre)
	
	
	
	Escribir 'Apellido paterno: ' Sin Saltar
	leer apellidoP
	VerificadorNombres(apellidoP)
	
	Escribir 'Apellido materno : ' Sin Saltar
	leer apellidoM
	VerificadorNombres(apellidoM)
	
	Escribir ''
	
	Escribir 'Fecha de Nacimiento(Formato: DD/MM/AAAA, Ejemplo : 03/05/2007 = 3 de Marzo de 2007): ' Sin Saltar
	leer fecha
	
	ValFecha <- VerificacionFecha(fecha)
	
	Mientras ValFecha  = Falso Hacer
		Escribir 'Fecha inválida, favor de reinsertar(Formato: DD/MM/AAAA, Ejemplo : 03/05/2007 = 3 de Marzo de 2007): ' Sin Saltar
		leer fecha
		ValFecha <- VerificacionFecha(fecha)
	FinMientras
	
	Escribir ''
	
	Escribir 'Sexo(H o M, H = hombre y M = mujer): ' Sin Saltar
	leer sexo 
	Verificadorsexo(sexo)
	
	Escribir 'Estado de nacimiento(Inserte el numero correspondiente, 1:AGUASCALIENTES, 2:BAJA CALIFORNIA, 3:BAJA CALIFORNIA SUR, '
	Escribir '4:CAMPECHE, 5:COAHUILA, 6:COLIMA, 7:CHIAPAS, 8:CHIHUAHUA, 9:CIUDAD DE MÉXICO, 10:DURANGO, 11:GUANAJUATO, 12:GUERRERO, '
	Escribir '13:HIDALGO, 14:JALISCO, 15:ESTADO DE MÉXICO, 16:MICHOACÁN, 17:MORELOS, 18:NAYARIT, 19:NUEVO LEÓN, 20:OAXACA, '
	Escribir '21:PUEBLA, 22:QUERÉTARO, 23:QUINTANA ROO, 24:SAN LUIS POTOSOSÍ, 25:SINALOA, 26:SONORA, 27:TABASCO, 28:TAMAULIPAS, '
	Escribir '29:TLAXCALA, 30:VERACRUZ, 31:YUCATÁN, 32:ZACATECAS, 33:NACIDO EN EL EXTRANJERO)'
	Leer estado
	VerificadorEstado(estado)
	
	aux <- ObtencionCurpComp(nombre,apellidoM,apellidoP,fecha,sexo,estado)
	
	Imprimir aux
	
FinProceso
