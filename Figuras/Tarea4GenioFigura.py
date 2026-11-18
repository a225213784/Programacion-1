# Nombre del archivo: Tarea4GenioFigura.py
# Descripción: Programa que solicita 2 parámetros para posteriormente dibujar una variedad de figuras usando estos mismos.
# Autores: Cristobal Ochoa Isibasi y Chrstian Alexandro Lopez (Grupo1)
# Fecha: 10/29/2026
# A lo largo del programa hay instancias de símbolo sin acento; cuando esto ocurra, a lo que nos estamos refiriendo es a la variable, no a la palabra.
#ComentarioGit
#Modificacion github; Descripción: Programa que solicita 2 parámetros para posteriormente dibujar una variedad de figuras usando estos mismos.



def DibujarMono(dim:int,simbolo:str) -> None:
    
    
    """
    Función que dibuja un moño usando símbolos..

    Parameters:
    
        dim (int): Número entero(5<=x<=151) que será usado para definir la dimensión de la figura a imprimir.
        simbolo (str): Cadena de caracteres de longitud uno que se usará como el símbolo con el que se dibujará la figura.

    Returns:
    
        None 

    Raises:
    
        ValueError: Si dim no se encuentra en el rango 5<=x<=151 o si simbolo no es de largo uno.
        TypeError: Si dim no es un entero o si simbolo no es una cadena.

    Examples:
    
        >>> DibujarMono(5,'G')
        G   G
        GG GG
        GGGGG
        GG GG
        G   G
        
        >>> DibujarMono(2,'G')
        Traceback (most recent call last):
        ValueError: Error, número inválido.
        

    """
    if not (isinstance(dim,int) and isinstance(simbolo,str)):
        raise TypeError('Error, tipo de dato inválido.')
    if not 5<=dim<=151:
        raise ValueError('Error, número inválido.')
    if len(simbolo) != 1:
        raise ValueError('Error, cadena inválida.')
    
   
    
    espacio = ' '
    dimmod = dim//2 + 1
    for i in range(1,dimmod):
        n = dim - 2*i
        print(f'{i*simbolo}{n*espacio}{i*simbolo:<}')
    
    print(dim*simbolo)
    
    for i in range(dimmod-1,0,-1):
        n = dim - 2*i
        print(f'{i*simbolo}{n*espacio}{i*simbolo:<}')


########################################################################################################################
def DibujarCopa(dim:int,simbolo:str) -> None :
    """
    Función que dibuja una copa usando símbolos..

    Parameters:
    
        dim (int): Número entero(5<=x<=151) que será usado para definir la dimensión de la figura a imprimir.
        simbolo (str): Cadena de caracteres de longitud uno que se usará como el símbolo con el que se dibujará la figura.

    Returns:
    
        None 

    Raises:
    
        ValueError: Si dim no se encuentra en el rango 5<=x<=151 o si simbolo no es de largo uno.
        TypeError: Si dim no es un entero o si simbolo no es una cadena.

    Examples:
    
        >>> DibujarCopa(5,'G')
        GGGGG
         GGG 
          G  
          G  
        GGGGG
       
        
        >>> DibujarCopa(2,'G')
        Traceback (most recent call last):
        ValueError: Error, número inválido.
        

    """
    if not (isinstance(dim,int) and isinstance(simbolo,str)):
        raise TypeError('Error, tipo de dato inválido.')
    if not 5<=dim<=151:
        raise ValueError('Error, número inválido.')
    if len(simbolo) != 1:
        raise ValueError('Error, cadena inválida.')
    
    
    
    
    
    for i in range(dim,0,-2):
        print(f'{i*simbolo:^{dim}}')
        
    
    
    dimmod = dim//2 - 1
    while i <= dimmod :
        print(f'{simbolo:^{dim}}')
        i += 1
    
    print(dim*simbolo)
###############################################################################################################################
def DibujarMonoVacio(dim:int,simbolo:str) -> None :
    """
    Función que dibuja un moño vacío usando símbolos..

    Parameters:
    
        dim (int): Número entero(5<=x<=151) que será usado para definir la dimensión de la figura a imprimir.
        simbolo (str): Cadena de caracteres de longitud uno que se usará como el símbolo con el que se dibujará la figura.

    Returns:
    
        None 

    Raises:
    
        ValueError: Si dim no se encuentra en el rango 5<=x<=151 o si simbolo no es de largo uno.
        TypeError: Si dim no es un entero o si simbolo no es una cadena.

    Examples:
    
        >>> DibujarMonoVacio(9,'G')
        G       G
        GG     GG
        G G   G G
        G  G G  G
        G   G   G
        G  G G  G
        G G   G G
        GG     GG
        G       G
        
        
        >>> DibujarMonoVacio(2,'G')
        Traceback (most recent call last):
        ValueError: Error, número inválido.
        

    """
    if not (isinstance(dim,int) and isinstance(simbolo,str)):
        raise TypeError('Error, tipo de dato inválido.')
    if not 5<=dim<=151:
        raise ValueError('Error, número inválido.')
    if len(simbolo) != 1:
        raise ValueError('Error, cadena inválida.')
    espacio = ' '
    dimmod = dim//2 + 1
    dimmod1 = dim//2  - 1
    for i in range(1,dimmod):
        n = dim - 2*i
        if i <= 2:
              print(f'{i*simbolo}{n*espacio}{i*simbolo:<}')
        else:
              m = i - 2 
              print(f'{simbolo}{m*espacio}{simbolo}{n*espacio}{simbolo:<}{m*espacio:<}{simbolo:<}')
            
    print(f'{simbolo}{dimmod1*espacio}{simbolo}{dimmod1*espacio}{simbolo}')
    
    for i in range(dimmod-1,0,-1):
        n = dim - 2*i
        if i <= 2:
            print(f'{i*simbolo}{n*espacio}{i*simbolo:<}')
        else:
            m = i - 2 
            print(f'{simbolo}{m*espacio}{simbolo}{n*espacio}{simbolo:<}{m*espacio:<}{simbolo:<}')
###############################################################################################################################
def DibujarCopaVacia(dim:int,simbolo:str) -> None:
    """
    Función que dibuja una copa vacía usando símbolos.

    Parameters:
    
        dim (int): Número entero(5<=x<=151) que será usado para definir la dimensión de la figura a imprimir.
        simbolo (str): Cadena de caracteres de longitud uno que se usará como el símbolo con el que se dibujará la figura.

    Returns:
    
        None 

    Raises:
    
        ValueError: Si dim no se encuentra en el rango 5<=x<=151 o si simbolo no es de largo uno.
        TypeError: Si dim no es un entero o si simbolo no es una cadena.

    Examples:
    
        >>> DibujarCopaVacia(5,'G')
        GGGGGGG
         G   G 
          G G 
           G   
           G   
           G   
        GGGGGGG
       
        
        >>> DibujarCopaVacia(2,'G')
        Traceback (most recent call last):
        ValueError: Error, número inválido.
        

    """
    if not (isinstance(dim,int) and isinstance(simbolo,str)):
        raise TypeError('Error, tipo de dato inválido.')
    if not 5<=dim<=151:
        raise ValueError('Error, número inválido.')
    if len(simbolo) != 1:
        raise ValueError('Error, cadena inválida.')
    
    t = -1
    for i in range(dim,0,-2):
        espacio = ' '
        t += 1
        if i == dim or i == 1:
            print(f'{i*simbolo:^{dim}}')
        else:
            m = i - 2
            print(f'{t*espacio}{simbolo}{m*espacio}{simbolo:>} ')
        
    
    
    dimmod = dim//2 - 1
    while i <= dimmod :
        print(f'{simbolo:^{dim}}')
        i += 1
    
    print(dim*simbolo)
###############################################################################################################################################################
def DibujarRombo(dim:int,simbolo:str) -> None:
    """
    Función que dibuja un rombo usando símbolos..

    Parameters:
    
        dim (int): Número entero(5<=x<=151) que será usado para definir la dimensión de la figura a imprimir.
        simbolo (str): Cadena de caracteres de longitud uno que se usará como el símbolo con el que se dibujará la figura.

    Returns:
    
        None 

    Raises:
    
        ValueError: Si dim no se encuentra en el rango 5<=x<=151 o si simbolo no es de largo uno.
        TypeError: Si dim no es un entero o si simbolo no es una cadena.

    Examples:
    
        >>> DibujarRombo(5,'G')
          G  
         GGG 
        GGGGG
         GGG 
          G  

        
        
        >>> DibujarRombo(2,'G')
        Traceback (most recent call last):
        ValueError: Error, número inválido.
        

    """
    
    
    
    if not (isinstance(dim,int) and isinstance(simbolo,str)):
        raise TypeError('Error, tipo de dato inválido.')
    if not 5<=dim<=151:
        raise ValueError('Error, número inválido.')
    if len(simbolo) != 1:
        raise ValueError('Error, cadena inválida.')
    
    for i in range(1,dim +1,2):
        print(f'{i*simbolo:^{dim}}')
    for j in range(dim-2,0,-2):
        print(f'{j*simbolo:^{dim}}')
########################################################################################################################################################################
def DibujarRomboVacio(dim:int,simbolo:str) -> None:
    """
    Función que dibuja un rombo vacío usando símbolos..

    Parameters:
    
        dim (int): Número entero(5<=x<=151) que será usado para definir la dimensión de la figura a imprimir.
        simbolo (str): Cadena de caracteres de longitud uno que se usará como el símbolo con el que se dibujará la figura.

    Returns:
    
        None 

    Raises:
    
        ValueError: Si dim no se encuentra en el rango 5<=x<=151 o si simbolo no es de largo uno.
        TypeError: Si dim no es un entero o si simbolo no es una cadena.

    Examples:
    
        >>> DibujarRomboVacio(5,'G')
          G  
         G G
        G   G
         G G
          G 
        
        
        >>> DibujarRomboVacio(2,'G')
        Traceback (most recent call last):
        ValueError: Error, número inválido.
        

    """
    
    
    
    
    if not (isinstance(dim,int) and isinstance(simbolo,str)):
        raise TypeError('Error, tipo de dato inválido.')
    if not 5<=dim<=151:
        raise ValueError('Error, número inválido.')
    if len(simbolo) != 1:
        raise ValueError('Error, cadena inválida.')
    espacio = ' '
    m = dim//2
    for i in range(1,dim +1,2):
        if i == 1 :
            print(f'{i*simbolo:^{dim}}')
        else:
            m -= 1
            t = i - 2
            print(f'{m*espacio}{simbolo}{t*espacio}{simbolo}')
            
    m = 0
             
    for j in range(dim-2,0,-2):
        if j == 1 :
            print(f'{simbolo:^{dim}}')
        else:
            m += 1
            t = j - 2
            print(f'{m*espacio}{simbolo}{t*espacio}{simbolo}')
####################################################################################################################################################################################
def DibujarRelojArena(dim:int,simbolo:str) -> None :
    """
    Función que dibuja un reloj de arena usando símbolos..

    Parameters:
    
        dim (int): Número entero(5<=x<=151) que será usado para definir la dimensión de la figura a imprimir.
        simbolo (str): Cadena de caracteres de longitud uno que se usará como el símbolo con el que se dibujará la figura.

    Returns:
    
        None 

    Raises:
    
        ValueError: Si dim no se encuentra en el rango 5<=x<=151 o si simbolo no es de largo uno.
        TypeError: Si dim no es un entero o si simbolo no es una cadena.

    Examples:
    
        >>> DibujarRelojArena(5,'G')
        GGGGG
         GGG 
          G  
         GGG 
        GGGGG
 

        
        
        >>> DibujarRelojArena(2,'G')
        Traceback (most recent call last):
        ValueError: Error, número inválido.
        

    """
    
    
    
    if not (isinstance(dim,int) and isinstance(simbolo,str)):
        raise TypeError('Error, tipo de dato inválido.')
    if not 5<=dim<=151:
        raise ValueError('Error, número inválido.')
    if len(simbolo) != 1:
        raise ValueError('Error, cadena inválida.')
    
    
    for j in range(dim,0,-2):
        print(f'{j*simbolo:^{dim}}')
    for i in range(3,dim +1,2):
        print(f'{i*simbolo:^{dim}}')
#######################################################################################################################################################################################
def DibujarRelojArenaVacio(dim:int,simbolo:str) -> None:
    """
    Función que dibuja un reloj de arena vacío usando símbolos..

    Parameters:
    
        dim (int): Número entero(5<=x<=151) que será usado para definir la dimensión de la figura a imprimir.
        simbolo (str): Cadena de caracteres de longitud uno que se usará como el símbolo con el que se dibujará la figura.

    Returns:
    
        None 

    Raises:
    
        ValueError: Si dim no se encuentra en el rango 5<=x<=151 o si simbolo no es de largo uno.
        TypeError: Si dim no es un entero o si simbolo no es una cadena.

    Examples:
    
        >>> DibujarRelojArenaVacio(7,'G')
        GGGGGGG
         G   G
          G G
           G   
          G G
         G   G
        GGGGGGG
        
        
        >>> DibujarRelojArenaVacio(2,'G')
        Traceback (most recent call last):
        ValueError: Error, número inválido.
        
    """
     
    espacio = ' '
     
    if not (isinstance(dim,int) and isinstance(simbolo,str)):
        raise TypeError('Error, tipo de dato inválido.')
    if not 5<=dim<=151:
        raise ValueError('Error, número inválido.')
    if len(simbolo) != 1:
        raise ValueError('Error, cadena inválida.')
     
    t = 0
    
    for j in range(dim,0,-2):
        if j == dim or j == 1:
            print(f'{j*simbolo:^{dim}}')
        else:
            t += 1
            m = j -2
            print(f'{t*espacio}{simbolo}{m*espacio}{simbolo}')
            
    t = dim//2
    for i in range(3,dim +1,2):
        if i == dim: 
            print(f'{i*simbolo:^{dim}}')
         
        else:
            t -= 1
            m = i - 2 
            print(f'{t*espacio}{simbolo}{m*espacio}{simbolo}')
######################################################################################################################################################
def SelectorDeVacioRelleno() -> bool:
    """
    Función que solicita un número con el rango (1 <= x <= 2) para posteriormente usarlo para asignar si las figuras han de ser vacías o rellenas. 

    Parameters:
        None
    
        
    Returns:
    
        bool : El valor de verdadero o falso del enunciado "La figura será dibujada vacía". 

    Raises:
    
        None

    Examples:
    
        >>> SelectorDeVacioRelleno()
        La figura será rellena o vacía
        1)Figura rellenada
        2)Figura vacía
        : 1
        
        
        
        
        >>> SelectorDeVacioRelleno()
        La figura será rellena o vacía
        1)Figura rellenada
        2)Figura vacía
        : 6
        Error, número inválido.
        : 2
        

    """
    
    
    
    print('La figura será rellena o vacía')
    print('1)Figura rellenada\n','\b2)Figura vacía')
    
    while True:
        try :
            n = int(input(': '))
            if 1<= n <=2:
                break
            else:
                print('Error, número inválido.')
        except Exception:
            print('Error, tipo de dato inválido.')
    
    
    
    if n == 2:
        return True
    return False
######################################################################################################################################################
def SelectorDimension() -> int:
    """
    Función que solicita un número con el rango (5 <= x <= 151) al usuario, que posteriormente se procesará y se le devolverá al proceso principal como una variable. 

    Parameters:
        None
    
        
    Returns:
    
        int : El valor asignado a la dimensión. 

    Raises:
    
        None

    Examples:
    
        >>> SelectorDimension()
        Inserte la dimensión; esta debe ser impar y mayor o igual a 5 y menor o igual a 151 : 7
        
        
        
        >>> SelectorDimension()
        Inserte la dimensión; esta debe ser impar y mayor o igual a 5 y menor o igual a 151 : 2
        Error, número inválido.
        Inserte la dimensión; esta debe ser impar y mayor o igual a 5 y menor o igual a 151 : 7

    """

    
    while True:
     try :
        dim = int(input('Inserte la dimensión; esta debe ser impar y mayor o igual a 5 y menor o igual a 151 : '))
        if 5<=dim<=151 and dim%2!=0:
            break
        else:
            print('Error, número inválido.')
     except Exception:
        print('Error, tipo de dato inválido.')
        
    return dim
######################################################################################################################################################    
def SelectorSimbolo() -> str:
    """
    Función que solicitará un solo carácter al usuario para posteriormente procesarlo y devolverlo a la función principal como una variable.

    Parameters:
        None
    
        
    Returns:
    
        str : El símbolo asignado. 

    Raises:
    
        None

    Examples:
    
        >>> SelectorSimbolo()
        Inserte el símbolo a evaluar, solo un símbolo y no puede ser un espacio : A
        
        
        
        >>> SelectorSimbolo()()
        Inserte el símbolo a evaluar, solo un símbolo y no puede ser un espacio : HO
        Error, cadena inválida.
        Inserte el símbolo a evaluar, solo un símbolo y no puede ser un espacio : 
        Error, cadena inválida.
        Inserte el símbolo a evaluar, solo un símbolo y no puede ser un espacio : A

    """
    
    while True:
        try:
            simbolo = input('Inserte el símbolo a evaluar, solo un símbolo y no puede ser un espacio : ')
            if len(simbolo) == 1 and simbolo != ' ':
                break
            else:
                print('Error, cadena inválida.')
        except Exception:
            print('Error, tipo de dato inválido.')
        
    return simbolo
#######################################################



while True:
    print()
    
    print('Este programa te ofrecerá ciertas figuras, que una vez seleccionadas, serán dibujadas bajo los siguientes parámetros.')
    
    print('''Selección de la figura:
0)Salir del programa
1)Reloj de arena
2)Rombo
3)Moño
4)Copa
5)Todos ''')
    
    while True:
     try:
        seleccion = int(input(':'))
        if 0<= seleccion <=5:
            break
        else:
            print('Error, número inválido.')
     except Exception:
        print('Error, tipo de dato inválido.')
        
    match seleccion:
        
        case 0:
            print('Saliendo del programa')
            break
        
        case 1:
            vacio = SelectorDeVacioRelleno()
            dim = SelectorDimension()
            simbolo = SelectorSimbolo()
            
            if vacio == True:
                print()
                DibujarRelojArenaVacio(dim,simbolo)
            else:
                print()
                DibujarRelojArena(dim,simbolo)
        case 2:
            vacio = SelectorDeVacioRelleno()
            dim = SelectorDimension()
            simbolo = SelectorSimbolo()
            
            if vacio == True:
                print()
                DibujarRomboVacio(dim,simbolo)
            else:
                print()
                DibujarRombo(dim,simbolo)
        case 3:
            vacio = SelectorDeVacioRelleno()
            dim = SelectorDimension()
            simbolo = SelectorSimbolo()
            
            if vacio == True:
                print()
                DibujarMonoVacio(dim,simbolo)
            else:
                print()
                DibujarMono(dim,simbolo)
        case 4:
            vacio = SelectorDeVacioRelleno()
            dim = SelectorDimension()
            simbolo = SelectorSimbolo()
            
            if vacio == True:
                print()
                DibujarCopaVacia(dim,simbolo)
            else:
                print()
                DibujarCopa(dim,simbolo)
        case 5:
            vacio = SelectorDeVacioRelleno()
            dim = SelectorDimension()
            simbolo = SelectorSimbolo()
            
            if vacio == True:
                print('Reloj de arena: ')
                print()
                DibujarRelojArenaVacio(dim,simbolo)
                print()
                print(dim*'#')
                print()
                print('Rombo: ')
                print()
                DibujarRomboVacio(dim,simbolo)
                print()
                print(dim*'#')
                print()
                print('Moño: ')
                print()
                DibujarMonoVacio(dim,simbolo)
                print()
                print(dim*'#')
                print()
                print('Copa: ')
                print()
                DibujarCopaVacia(dim,simbolo)
                print()
             
            else:
                print('Reloj de arena: ')
                print()
                DibujarRelojArena(dim,simbolo)
                print()
                print(dim*'#',)
                print()
                print('Rombo: ')
                print()
                DibujarRombo(dim,simbolo)
                print()
                print(dim*'#')
                print()
                print('Moño: ')
                print()
                DibujarMono(dim,simbolo)
                print()
                print(dim*'#')
                print()
                print('Copa: ')
                print()
                DibujarCopa(dim,simbolo)
                print()
                
             
        
            
    
    

        

    
    








    
