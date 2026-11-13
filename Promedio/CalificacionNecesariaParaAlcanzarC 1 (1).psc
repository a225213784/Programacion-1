//Titulo: OperaciónRescate.psc
//Descripción: En este programa se calculará la calificación necesaria para obtener un promedio sobresaliente (90 o mas), promedio regular (Entre 60 y 90), o promedio suficiente para aprobar la materia (60) en base a el promedio de los anteriores 3 examenes y al final mostrará la cantidad de alumnos potenciales a un promedio sobresaliente, regular, suficiente y los que inevitablemente reprobarán.
//Autor: Cristobal Ochoa Isibasi y Christian Alexandro Grupo#1
//Fecha 19/09/2026

Proceso OperacionRescate
	Definir numEstudiantes, examen1, examen2, examen3, promedioActual, promedioSobresaliente, minimoparaPRegular,maximoparaPRegular, promedioSuficiente, posiblesSobresalientes, posiblesRegulares, posiblesSuficientes, reprobadosInevitable, i Como Entero
	
	//Encabezado
	Escribir "En este programa se calculará la calificación necesaria para obtener un promedio sobresaliente (90 o más), promedio regular (entre 61 y 89) o un promedio suficiente para aprobar la materia (60) con base en el promedio de los anteriores 3 exámenes y, al final, mostrará la cantidad de alumnos con el potencial de obtener un promedio sobresaliente, regular, suficiente y los que inevitablemente reprobarán."


	
	Escribir ""
	
	//Estudiantes a evaluar
	Escribir Sin Saltar "¿Cuántos alumnos hay en el aula? "
	Leer numEstudiantes
	
	//Filtro para el numero de estudiantes 
	Mientras numEstudiantes <= 0 Hacer
		Escribir "Número de estudiantes inválido, favor de reinsertar"
		Escribir " " 
		Escribir Sin Saltar "¿Cuántos alumnos hay en el aula? "
		Leer numEstudiantes
	FinMientras
	Escribir ""
	
	i <- 1
	reprobadosInevitable <- 0
	posiblesSuficientes <- 0
	posiblesRegulares <- 0
	posiblesSobresalientes <- 0
	
	Mientras i <= numEstudiantes Hacer
		Escribir Sin Saltar "Ingrese la calificación del primer examen del alumno ", i, ":"
		Leer examen1
		Mientras examen1 > 100 o examen1 < 0 Hacer
			Escribir "Calificación inválida, favor de reinsertar."
			Escribir ""
			Escribir Sin Saltar "Ingrese la calificación del primer examen del alumno ", i, ":"
			Leer examen1
		FinMientras
		
		Escribir Sin Saltar "Ingrese la calificación del segundo examen del alumno ", i, ":"
		Leer examen2
		Mientras examen2 > 100 o examen2 < 0 Hacer
			Escribir "Calificación inválida, favor de reinsertar."
			Escribir ""
			Escribir Sin Saltar "Ingrese la calificación del segundo examen del alumno ", i, ":"
			Leer examen2
		FinMientras
		
		Escribir Sin Saltar "Ingrese la calificación del tercer examen del alumno ", i, ":"
		Leer examen3
		Mientras examen3 > 100 o examen3 < 0 Hacer
			Escribir "Calificación inválida, favor de reinsertar."
			Escribir ""
			Escribir Sin Saltar "Ingrese la calificación del tercer examen del alumno ", i, ":"
			Leer examen3
		FinMientras
		
		Escribir ""
		
		//Promedio actual en base a los 3 examenes ya presentados
		promedioActual <- redon((examen1 + examen2 + examen3) / 3)
		Escribir "El promedio actual del alumno ", i, " es de ", promedioActual
		
		Escribir ""
		//Despejamos la calificación necesaria para obtener un promedio suficiente mediante la resta de las calificaciones obtenidas previamente a 240 que es lo que se necesita para obtener promedio de 60.
		promedioSuficiente <- 240 - examen1 - examen2 - examen3
		Si promedioSuficiente <= 100 Entonces
			Escribir "Promedio Suficiente: Meta alcanzable"
		SiNo;
			Escribir "Promedio Suficiente: Meta no alcanzable"
		FinSi
		Si promedioSuficiente <= 0 Entonces
			Escribir "El alumno ya tiene asegurado un promedio de 60."
		FinSi
		
		Si promedioSuficiente <= 100 y promedioSuficiente > 0  Entonces
			Escribir "Necesita obtener una calificación de más de o igual a ", promedioSuficiente, " en el cuarto examen para obtener un promedio de  60."
		FinSi
		Escribir ""
		
		//Despejamos el rango de calificación para obtener un promedio regular, a 244 se le resta las calificaciones obtenidas previamente porque 244 es la calificacion necesaria entre todos los examenes para obtener un promedio de 61 y para obtener un promedio de 89 es de 356 por lo tanto para obtener un promedio regular debes sacar una calificación entre ese rango.
		minimoparaPRegular <- 244 - examen1 - examen2 - examen3
		maximoparaPRegular <- 356 - examen1 - examen2 - examen3
		Si minimoparaPRegular <= 100 Entonces
			Escribir "Promedio Regular: Meta alcanzable"
		SiNo
			Escribir "Promedio Regular: Meta no alcanzable"
		FinSi
		Si minimoparaPRegular < 0 y maximoparaPRegular <= 100 Entonces
			Escribir "La calificación que se necesita obtener en el cuarto examen para hacer que el estudiante permanezca en el rango (61-89) es igual o menor a ", maximoparaPRegular + 3 
		FinSi
		Si minimoparaPRegular <= 0  y maximoparaPRegular > 100 Entonces
			Escribir "El estudiante forzosamente quedará en este rango (61-89) (independiente de la calificación obtenida en el cuarto examen)."
		FinSi
		Si minimoparaPRegular <= 100 y minimoparaPRegular > 0  Entonces
			Escribir "La calificación que se necesita obtener en el cuarto examen para obtener un promedio regular (61-89) es igual o mayor a ", minimoparaPRegular
			
		FinSi
		
		Escribir ""
		
		//Despejamos cuanto se necesita para sacar un promedio de 90 mediante la resta hacia el 360 ya que si se ponen 4 examenes entonces si sacas 90 en las 4 eso da 360 y ese 360 cuando se divide entre 4 da el resultado de promedio de 90
		promedioSobresaliente <- 360 - examen1 - examen2 - examen3
		Si promedioSobresaliente <= 100 Entonces
			Escribir "Promedio Sobresaliente: Meta alcanzable"
		SiNo
			Escribir "Promedio Sobresaliente: Meta no alcanzable"
		FinSi
		
		Si promedioSobresaliente <= 100 Entonces
			Escribir "La calificación que se necesita obtener en el examen 4 para obtener un promedio sobresaliente es mayor o igual a  ", promedioSobresaliente
		FinSi
		
		Escribir ""
		
	

		Si promedioSobresaliente <= 100 Entonces
			posiblesSobresalientes <- posiblesSobresalientes + 1
			Escribir "El alumno#',i," tiene la posibilidad de obtener un promedio sobresaliente"
			
		SiNo
			Si promedioActual >= 60 Y minimoparaPRegular <= 100 Entonces
				posiblesRegulares <- posiblesRegulares + 1
				Escribir "El alumno#',i," tiene la posibilidad de obtener un promedio regular"
				
			SiNo
				Si promedioActual < 60 Y promedioSuficiente <= 100 Entonces
					posiblesSuficientes <- posiblesSuficientes + 1
					Escribir "El alumno#',i," tiene la posibilidad de aprobar el semestre"
					
				SiNo
					reprobadosInevitable <- reprobadosInevitable + 1
					Escribir "El alumno#',i," esta reprobado"
				FinSi
			FinSi
		FinSi
		i <- i + 1
		
		Escribir ""
		
	FinMientras
	
	Escribir "El número de alumnos que inevitablemente reprobarán son ", reprobadosInevitable, " alumnos."
	Escribir "El número de alumnos que pueden salvar la materia son ", posiblesSuficientes, " alumnos."
	Escribir "El número de alumnos que pueden obtener un promedio regular son ", posiblesRegulares, " alumnos."
	Escribir "El número de alumnos que pueden obtener un promedio sobresaliente son ", posiblesSobresalientes, " alumnos."
	
FinProceso

//Le agregue los filtros que le faltaban (estudiantes y calificaciones)
