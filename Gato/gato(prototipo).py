import numpy as np

gato = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]],str)

print(gato)




def cambiarvalor(n:int,turno:int,gato) -> list:

     match n:
        
    
        case 1:
            if (gato[0,0]) != 'x' and  (gato[0,0]) != 'o'  and turno == 0 :
                gato[0,0] = 'o'
                validez = 1
            if (gato[0,0]) != 'x' and  (gato[0,0]) != 'o'  and turno == 0 :
                gato[0,0] = 'x'
                validez = 1
        case 2:
            if (gato[0,1]) != 'x' and  (gato[0,1]) != 'o'  and turno == 0 :
                gato[0,1] = 'o'
                validez = 1
            if (gato[0,1]) != 'x' and  (gato[0,1]) != 'o'  and turno == 1 :
                gato[0,1] = 'x'
                validez = 1
        case 3:
             if (gato[0,2]) != 'x' and  (gato[0,2]) != 'o'  and turno == 0 :
                gato[0,2] = 'o'
                validez = 1
             if (gato[0,2]) != 'x' and  (gato[0,2]) != 'o'  and turno == 1 :
                gato[0,2] = 'x'
                validez = 1
        case 4:
             if (gato[1,0]) != 'x' and  (gato[1,0]) != 'o'  and turno == 0 :
                gato[1,0] = 'o'
                validez = 1
             if (gato[1,0]) != 'x' and  (gato[1,0]) != 'o'  and turno == 1 :
                gato[1,0] = 'x'
                validez = 1
        case 5:
             if (gato[1,1]) != 'x' and  (gato[1,1]) != 'o'  and turno == 0 :
                gato[1,1] = 'o'
                validez = 1
             if (gato[1,1]) != 'x' and  (gato[1,1]) != 'o'  and turno == 1 :
                gato[1,1] = 'x'
                validez = 1
        case 6:
             if (gato[1,2]) != 'x' and  (gato[1,2]) != 'o'  and turno == 0 :
                gato[1,2] = 'o'
                validez = 1
             if (gato[1,2]) != 'x' and  (gato[1,2]) != 'o'  and turno == 1 :
                gato[1,2] = 'x'
                validez = 1
        case 7:
             if (gato[2,0]) != 'x' and  (gato[2,0]) != 'o'  and turno == 0 :
                gato[2,0] = 'o'
                validez = 1
             if (gato[2,0]) != 'x' and  (gato[2,0]) != 'o'  and turno == 1 :
                gato[2,0] = 'x'
                validez = 1
        case 8:
             if (gato[2,1]) != 'x' and  (gato[2,1]) != 'o'  and turno == 0 :
                gato[2,1] = 'o'
                validez = 1
             if (gato[2,1]) != 'x' and  (gato[2,1]) != 'o'  and turno == 1 :
                gato[2,1] = 'x'
                validez = 1
        case 9:
             if (gato[2,2]) != 'x' and  (gato[2,2]) != 'o'  and turno == 0 :
                gato[2,2] = 'o'
                validez = 1
             if (gato[2,2]) != 'x' and  (gato[2,2]) != 'o'  and turno == 1 :
                gato[2,2] = 'x'
                validez = 1
     print(gato)
     return gato








def Victoria(gato,simbolo) -> bool :
    for i in range(3):
        puntaje = 0
        
        for j in range(3):
         if (gato[i,j] == simbolo):
             puntaje += 1
         if puntaje == 3:
          print(1)
          return True 
         
        
    for i in range(3):
        puntaje = 0
        for j in range(3):
         if (gato[j,i] == simbolo ):
             puntaje += 1
         if puntaje == 3:
             print(2)
             return True
    
    puntajel = 0
           
    for i in range(3):
        if (gato[0,0] == simbolo ) and gato[1,1] == simbolo and gato[2,2] == simbolo:
             print(3)
             return True 
        for j in range(3):
            if (gato[0,2] == simbolo) and gato[1,1] == simbolo and  gato[2,0] == simbolo: 
                return True
    return False
            
        
cont = 1 
while True :
    eleccion = int(input(':'))
    turno = 0
    simbolo = 'o'
    if cont%2 == 0:
        turno = 1
        simbolo = 'x'
    gato = cambiarvalor(eleccion,turno,gato)
    terminarjuego = Victoria(gato,simbolo)
    
    if terminarjuego == True and cont%2 == 1:
        print('Gano el jugador bola')
        break
    elif terminarjuego == True and cont%2 == 0:
        print('Gano el jugador cruz')
        break
    elif cont == 10 :
        print("Quedo empate")
        break
    cont += 1
        



























       
    
            

