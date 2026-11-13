//Nombre del archivo: Una cuestión de peso 
//Autores:Cristobal Ochoa y Christian Alexandro Lopez 
//Fecha: 28/08/2026
//Descripción: Algoritmo que, una vez insertados un peso, edad y altura válidos, calcula el índice de masa corporal y lo clasifica.


Proceso NombreCalculadorIMC
	
	//Definición de variables a usar
	Definir peso,altura, imc Como Real
	Definir edad Como Entero
	Definir imcr Como Caracter
	
	
	//Introducción del programa al usuario  
    Escribir 'Este programa, una vez insertados los datos que se le pedirán posteriormente, calcula tu imc para después clasificarlas conforme a las categorías impuestas por la OMS.(Este programa está diseñado para adultos de por lo menos 20 años)'
	Escribir ''
	Escribir 'Favor de insertar los siguientes datos.'
	
	//Input del usuario acerca de su edad y su posterior comprobación. (Los '' cumplen la función de dar un renglón de separación)
	Escribir ''
	Escribir 'Edad: ' Sin Saltar
	leer edad
	
	//Vi que si ponias una edad menor de 20 el programa se seguia ejecutando y lo corregí metiendo el código dentro del primer si condicional donde el código se ejecutará en caso de que la edad sea mayor o igual a 20.
	Si edad >= 20 Entonces
		//Input del usuario acerca de su altura y su posterior comprobación
		Escribir ''
		Escribir 'Altura(m): 'Sin Saltar
		Leer altura
		Si altura > 0 Entonces
			
			//Input del usuario acerca de su peso y posterior comprobación
			Escribir ''
			Escribir 'Peso(kg): ' Sin Saltar
			Leer peso
			Si peso > 0 Entonces
				
				//Calculadora de IMC
				imc<-peso/altura^2
				
				//Clasificador de IMC
				Si imc < 16.5 Entonces
					imcr<-'bajo peso severo'
				FinSi
				Si imc >= 16.5 y imc < 18.5 Entonces
					imcr<-'bajo peso'
				FinSi
				Si imc >= 18.5 y imc < 25 Entonces
					imcr<-'peso saludable'
				FinSi
				Si imc >= 25 y imc < 30 Entonces
					imcr<-'sobrepeso'
				FinSi
				Si imc >= 30 y imc < 35 Entonces
					imcr<-'obesidad tipo 1 (moderada)'
				FinSi
				Si imc >= 35 y imc < 40 Entonces
					imcr<-'obesidad tipo 2 (severa)'
				FinSi
				Si imc >= 40 Entonces
					imcr<-'obesidad tipo 3 (morbida)'
					
				FinSi
				
				//Presentación del IMC y su rango 
				Escribir ''
				Escribir 'Su IMC es equivalente a ',imc,' y este se encuentra en el rango de ',imcr,'.'
				
				
				
			SiNo
				
				//Situación donde el peso es inválido.
				Escribir ''
				Escribir 'El peso insertado es inválido.'
				
				
				
				
				
			FinSi
		SiNo
			// Situación donde el usuario inserta una altura inválida
			Escribir ''
			Escribir 'La altura insertada es inválida.'
			
			
			
		
		FinSi
		
		
	SiNo
		
		//Situación donde el usuario ingrese una edad menor que 20
		Escribir ''
		Escribir 'La edad insertada es inválida. (recuerde que este programa está diseñado para adultos de por lo menos 20 años'
		
		
	FinSi
	
FinProceso
