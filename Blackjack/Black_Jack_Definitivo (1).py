# Nombre del archivo: Black_Jack_Definitivo.py
# Descripción: Programa que te permite jugar al blackjack, dándole uso a la librería CustomTkinter.
# Autores: Cristobal Ochoa Isibasi y Christian Alexandro Lopez (Grupo1)
# Fecha: 11/9/2026
#Modificacion Git 


#Se está utilizando CustomTkinter para crear la interfaz gráfica. (https://customtkinter.tomschimansky.com/)
import customtkinter as ctk
import random



#Configuración de la ventana
ventana = ctk.CTk()
ventana.title("Black Jack")
ventana.geometry("800x800")
ventana.resizable(True, True)
ventana.configure(fg_color="#075B3B")


#Variable que guardará la configuración del título.
titulo = ctk.CTkLabel(ventana,text="BLACK JACK",font=("Georgia", 98, "bold"),text_color="#F5D77A")
titulo.pack(pady=(20, 0))

#Etiqueta Label para mostrar mensajes en pantalla
estado_label = ctk.CTkLabel(ventana, text="",font=("Georgia", 38, "bold"), text_color="white")
estado_label.pack()

#Área donde se dibujarán las cartas.
area_cartas = ctk.CTkFrame(ventana, fg_color="transparent")
area_cartas.pack(fill="both", expand=True, padx=40, pady=10)
AnchoCarta = 88
AlturaCarta = 132


#BlackJack Natural
def TieneBlackjackNatural(mano:list[tuple[str, str]]) -> bool:
    """
    Description:
    
        Indica si las dos cartas iniciales forman un Blackjack natural.
    
    Parameters:
    
        mano(list[tuple[str, str]]): Es la mano que va a revisar si tiene blackjack al iniciar la partida.
    Raise:
        TypeError: Si la variable mano no es una lista compuesta por tuplas que contienen strs.
        ValueError: Si las tuplas contenidas en la lista tienen más de dos elementos o si estos mismos elementos no pertenecen a las denominaciones
                    y palos previamente mencionados.
    
    Return:
    
        bool: Regresa un True si se tiene Black Jack al iniciar la partida y un False en caso contrario.
    
    """
    if not isinstance(mano,list):
        raise TypeError("La variable mano contiene un tipo de dato incompatible.")
    else:
        for carta in mano:
            if not isinstance(carta,tuple):
                raise TypeError("La variable mano contiene un tipo de dato incompatible.")
            else:
                if len(carta) != 2:
                    raise ValueError("La variable mano contiene una cantidad de elementos mayor a la esperada")
                else:
                    palo,denom = carta
                    if not (isinstance(palo,str) or isinstance(denom,str)):
                        raise TypeError("La variable mano contiene un tipo de dato incompatible.")
                    else:
                        if palo not in ['♥', '♦', '♣', '♠'] or denom not in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                            raise ValueError('Los elementos de la variable mano no coinciden con los conjuntos definidos como válidos')
            
  
    
    
    if len(mano) != 2:
        return False

    valores = [carta[1] for carta in mano]
    return (("A" in valores) and any(valor in ("10", "J", "Q", "K") for valor in valores))



#Inicio de Partida
def NuevaPartida() -> None:
    """
    Description:
    
        Crea y mezcla la baraja, reparte dos cartas a cada participante, reinicia el estado y actualiza la mesa y los botones.

    Parameters:
    
        No Parameters
    
    Raises:
        None 

    Returns:
    
        None:(Modifica las variables globales cada vez que inicia partida; por ejemplo, la baraja la revuelve de nuevo cada inicio.)
    """
    global baraja, mano_jugador, mano_crupier, estado, mensaje
    
    # Creación de la baraja.
    palos = ['♥', '♦', '♣', '♠']
    denominaciones = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    baraja = []
    for pal in palos:
        for denom in denominaciones:
            baraja.append((pal,denom))
    random.shuffle(baraja)


    #Le va a dar 2 cartas a cada jugador de la partida.
    mano_jugador = [RepartirCarta(baraja), RepartirCarta(baraja)]
    mano_crupier = [RepartirCarta(baraja), RepartirCarta(baraja)]
    
    blackjack_jugador = TieneBlackjackNatural(mano_jugador)
    blackjack_crupier = TieneBlackjackNatural(mano_crupier)

    if blackjack_jugador and blackjack_crupier:
        estado = "terminada"
        mensaje = "Empate: Ambos tienen Blackjack natural."
        boton_estado = "normal" if estado == "jugador" else "disabled"
        jalar.configure(state=boton_estado)
        plantarse.configure(state=boton_estado)
        estado_label.configure(text=mensaje)
        DibujarMesa()
        
    elif blackjack_crupier:
        estado = "terminada"
        mensaje = "El crupier tiene Blackjack natural. Gana el crupier."
        boton_estado = "normal" if estado == "jugador" else "disabled"
        jalar.configure(state=boton_estado)
        plantarse.configure(state=boton_estado)
        estado_label.configure(text=mensaje)
        DibujarMesa()
        
    elif blackjack_jugador:
        estado = "terminada"
        mensaje = "¡Blackjack natural! Ganaste."
        boton_estado = "normal" if estado == "jugador" else "disabled"
        jalar.configure(state=boton_estado)
        plantarse.configure(state=boton_estado)
        estado_label.configure(text=mensaje)
        DibujarMesa()

        
        
    else:
        estado = "jugador"
        mensaje = "Tu turno."
        
        #Estas líneas de código son para configurar si los botones funcionarán o no; esto sirve para que cuando acabe una partida, tengas que darle a 'Nuevo juego' para que funcionen los botones.      
        jalar.configure(state="normal")
        plantarse.configure(state="normal")
        estado_label.configure(text=mensaje)
        DibujarMesa()


        
        





######################################################################################################################################################################
#Dibujar la carta en la pantalla
######################################################################################################################################################################

def DibujarCarta(carta:tuple[str,str], x:int, y:int, oculta=False  ) -> None:
    """
    Description:
    
        Dibuja una carta en la mesa; si oculta es True, muestra el reverso.
    
    Parameters:
    
        carta(tuple[str, str]): palo y valor de la carta.
        x(int): posición horizontal donde se dibujarà la carta.
        y(int): posición vertical donde se dibujarà la carta.
    
    Raises:
        TypeError: Si las variables x e y no son int o si la variable carta no es una tupla compuesta por dos cadenas.
        ValueError: Si las cadenas contenidas en la tupla no coinciden con los siguientes conjuntos: palos = ['♥', '♦', '♣', '♠'] o denom = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    Returns:
    
        None:(Dibuja los elementos en la interfaz.)
        
    """
    if not isinstance(carta,tuple):
        raise TypeError("La variable carta contiene un tipo de dato incompatible.")
    else:
        if len(carta) != 2:
            raise ValueError("La variable mano contiene una cantidad de elementos mayor a la esperada")
        else:
            palo,denom = carta
            if not (isinstance(palo,str) or isinstance(denom,str)):
                raise TypeError("La variable carta contiene un tipo de dato incompatible.")
            else:
                if palo not in ['♥', '♦', '♣', '♠'] or denom not in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                    raise ValueError("Los valores contenidos en la variable carta son inválidos")
    if not isinstance(x,int):
        raise TypeError("La variable x contiene un tipo de dato incompatible.")
    if not isinstance(y,int):
        raise TypeError("La variable y contiene un tipo de dato incompatible.")
    if not isinstance(oculta,bool):
        raise TypeError("La variable 'oculta' contiene un tipo de dato incompatible.")
    
    
    #Extrae los valores de la tupla 'carta' para asignarle el primer valor de la tupla a palo y el segundo a valor.
    palo, valor = carta
    
    #Configura el color de los elementos de la carta con base en el palo que tiene.
    color_palo = "#D00" if palo in ("♥", "♦") else "#111111"

    #Rectángulo que simulará ser el fondo donde se escribe el valor y los palos de la carta (lienzo).
    rectanguloCartas = ctk.CTkFrame(
        area_cartas,
        width=AnchoCarta,
        height=AlturaCarta,
        fg_color="#174A73" if oculta else "white",
        border_color="#174A73" if oculta else "black",
        border_width=2,
        corner_radius=8,)
    
    rectanguloCartas.place(x=x, y=y)
    
    #Va a ocultar la segunda carta del crupier
    if oculta:
        ctk.CTkLabel(
            rectanguloCartas,
            text="BJ",
            text_color="#F5D77A",
            fg_color="transparent",
            font=("Georgia", 24, "bold"),
        ).place(relx=0.5, rely=0.5, anchor="center")
        return

    #Escribe las denominaciones en las esquinas de la carta
    ctk.CTkLabel(
        rectanguloCartas,
        text=valor,
        text_color=color_palo,
        fg_color="transparent",
        font=("Georgia", 23, "bold"),
        justify="right"
    ).place(relx=1, rely=1, anchor="se", x=-8, y=-8)
    
    ctk.CTkLabel(
        rectanguloCartas,
        text=valor,
        text_color=color_palo,
        fg_color="transparent",
        font=("Georgia", 23, "bold"),
        justify="right"
    ).place(x=124, y=82)
    
    ctk.CTkLabel(
        rectanguloCartas,
        text=valor,
        text_color=color_palo,
        fg_color="transparent",
        font=("Georgia", 23, "bold"),
        justify="left"
    ).place(x=8, y=6)
    
    

    #Escribe los palos en el centro de la carta
    ctk.CTkLabel(
        rectanguloCartas,
        text=palo,
        text_color=color_palo,
        fg_color="transparent",
        font=("Segoe UI Symbol", 50, "bold")
    ).place(relx=0.5, rely=0.50, anchor="center")






######################################################################################################################################################################
#Dibuja la mesa/lienzo donde se pondrán las cartas.
######################################################################################################################################################################

def DibujarMesa() -> None:
    """
    Description:
    
        Limpia y vuelve a dibujar las cartas y los títulos de la mesa según el estado de la partida.
    
    Parametros:
    
        None 
    
    Raises:
        
        None
        
    Returns:
    
        None:(Actualiza el juego cada vez que se realiza una acción; por ejemplo, al jalar, esto borra las cartas y llama a la función DibujarCarta para agregar la carta recién jalada.)"""
        
    # Elimina las cartas y títulos anteriores
    for widget in area_cartas.winfo_children():
        widget.destroy()
            
    if estado == "jugador":
        texto_crupier = "Crupier (una carta oculta)"
    else:
        texto_crupier = "Crupier"

    texto_jugador = "Jugador"

    #Texto arriba de las cartas que indicará de quienes son las cartas. 
    ctk.CTkLabel(
        area_cartas,
        text=texto_crupier,
        text_color="white",
        font=("Georgia", 16, "bold"),
    ).place(x=40, y=8)

    #El crupier va a dejar tapada su segunda carta durante el turno del jugador.
    x = 40
    for indice, carta in enumerate(mano_crupier):
        oculta = estado == "jugador" and indice == 1
        DibujarCarta(carta, x, 38, oculta=oculta)
        x += AnchoCarta + 15

    ctk.CTkLabel(
        area_cartas,
        text=texto_jugador,
        text_color="white",
        font=("Georgia", 16, "bold"),
    ).place(x=40, y=215)

    x = 40
    for carta in mano_jugador:
        DibujarCarta(carta, x, 245)
        x += AnchoCarta + 15
        
        
######################################################################################################################################################################
# Función para extraer una carta del mazo y entregársela a uno de los jugadores
######################################################################################################################################################################

def RepartirCarta(baraja:list[tuple[str,str,]]) -> list[tuple[str,str]]:
    """
    Description:
            
        Quita y devuelve la última carta de la baraja.
        
    Parameters:
        
        baraja(list[tuple[str, str]]): cartas disponibles para repartir; la función modifica esta lista.
    Raise:
        TypeError: Si la variable baraja no es una lista compuesta por tuplas 
        IndexError: Si la variable baraja ya no contiene más elementos 
        
    Returns:
        
        tuple[str, str]: la carta extraída.
    """
    if not isinstance(baraja,list):
        raise TypeError("La variable mano contiene un tipo de dato incompatible.")
    
    else:
        for carta in baraja:
            if not isinstance(carta,tuple):
                raise TypeError("La variable mano contiene un tipo de dato incompatible.")
            else:
                palo, denom = carta
                if not( isinstance(palo,str) or isinstance(denom,str)):
                    raise TypeError("La variable mano contiene un tipo de dato incompatible.")
    
    if len(baraja) == 0:
        raise IndexError()
            
                
        
    
    carta = (baraja.pop(-1))
    return carta

######################################################################################################################################################################
#La función que asigna el puntaje correspondiente.
######################################################################################################################################################################

def ValorCarta(valor:str) -> int:
    """
    Description:

        Convierte las figuras J, K y Q en 10, y el as en 11. Para otros valores, devuelve el valor recibido.
    
    Parameters:
    
        valor(str): denominación de la carta.
    Raise:
        TypeError: Si valor no es tipo str.
        ValueError: Si valor no pertenece a la siguiente lista de caracteres : ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] 
        
    Returns:
    
        valor(int) = Valor asignado a la carta
    """
    if not isinstance(valor,str):
        raise TypeError("La variable valor contiene un tipo de dato incompatible.")
    if valor not in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        raise ValueError("El valor de la variable 'valor' es inválido.")
  
    FaceCards = 'JKQ'
    if valor in FaceCards:
        valor = 10
    elif valor == 'A':
        valor = 11
    else:
        valor = valor
    return valor

######################################################################################################################################################################
#Función que gestiona los ases
######################################################################################################################################################################

def GestionadorAs(puntaje:int, numases:int) -> int:
    """
    Description:
    
        Reduce el valor de los ases de 11 a 1 mientras el puntaje supere 21.    
    
    Parameters:
    
        puntaje(int): puntaje actual de la mano.
        numases(int): cantidad de ases que puede ajustar.
    Raise:
        TypeError: Si las variables puntaje y numases no son int
        ValueError: Si (numases < 0 y numases > 4)  o  puntaje < 0.
        
    Returns:
    
        puntaje(int): El puntaje ajustado.
    """
    if not isinstance(puntaje,int):
        raise TypeError("La variable puntaje contiene un tipo de dato incompatible.")
    if not isinstance(numases,int):
        raise TypeError("La variable numases contiene un tipo de dato incompatible.")
    if puntaje < 0 :
        raise ValueError("El valor de la variable puntaje es inválido.")
    if numases < 0 or numases > 4 :
        raise ValueError("El valor de la variable numases es inválido.")



    if numases > 0 :
        i = 1
        
        while puntaje > 21 and i <= numases:
            puntaje = puntaje - 10
            i += 1
    return puntaje

######################################################################################################################################################################
#Función que gestiona el proceso de asignar un valor a cada carta jalada.
######################################################################################################################################################################

def AgregarCarta(carta:tuple[str,str]) -> int:
    """
    Description:
        
        Agrega una carta y le asigna un valor numérico.
        
        
            
    Parameters:
    
        carta(tuple[str, str]): carta de la que se calculará el valor.
    Raise:
        TypeError: Si la carta no es una tupla compuesta por string
        ValueError: Si las cadenas contenidas en la tupla no coinciden con los siguientes conjuntos: palos = ['♥', '♦', '♣', '♠'] o denom = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        
        
    Returns:
    
        valor(int): El valor numérico de la carta

    """
    if not isinstance(carta,tuple):
        raise TypeError("La variable carta contiene un tipo de dato incompatible.")
    else:
        for elemento in carta:
            if not isinstance(elemento,str):
                raise TypeError("La variable carta contiene un tipo de dato incompatible.")
    if len(carta) != 2:
        raise ValueError("La variable carta contiene una cantidad de elementos mayor a la esperada")
            
    palo,denom = carta
    if palo not in ['♥', '♦', '♣', '♠'] or denom not in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        raise ValueError("Los valores contenidos en la variable carta son inválidos")

    valor = int(ValorCarta(carta[1]))
    return valor

######################################################################################################################################################################
#Función que determina cuántos ases tiene la mano.
######################################################################################################################################################################

def ContarAses(carta:tuple[str,str],numas:int) -> int:
    """
    Description:
        
        Aumenta el contador si la carta es un as; en caso contrario, lo deja igual.            
    
    Parameters:
    
        carta(tuple[str, str]): carta que se revisará.
        numas(int): cantidad de ases contados hasta ese momento.
    Raises:
        TypeError: Si carta no es una tupla que contiene cadenas o si numas no es un int
        ValueError: Si las cadenas contenidas en la tupla no coinciden con los siguientes conjuntos: palos = ['♥', '♦', '♣', '♠'] o denom = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
                    Si numas es menor a 0 o mayor a 4
        
    Returns:
    
        int: devuelve el contador de as actualizado.
    """
    if not isinstance(carta,tuple):
        raise TypeError("La variable carta contiene un tipo de dato incompatible.")
    else:
        for elemento in carta:
            if not isinstance(elemento,str):
                raise TypeError("La variable carta contiene un tipo de dato incompatible.")
    if len(carta) != 2:
        raise ValueError("La variable carta contiene una cantidad de elementos mayor a la esperada")
            
    palo,denom = carta
    
    if palo not in ['♥', '♦', '♣', '♠'] or denom not in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        raise ValueError("Los valores contenidos en la variable carta son inválidos")
    if not isinstance(numas,int):
        raise TypeError()
    if numas < 0 or numas > 4:
        raise ValueError("El valor de la variable numas es inválido.")
    
    
    if carta[1] == 'A':
        return numas + 1
    else:
        return numas

######################################################################################################################################################################
#Función que gestiona el botón 'Jalar'.
######################################################################################################################################################################

def JalarCarta():
    """
    Description:
        
        Reparte una carta al jugador, recalcula su puntaje y determina si debe terminar la partida.    
   
    Parameters:
    
        No Parameters
    
    Raise:
        
        None
        
    Returns:
    
        None:(Llama a otras funciones, actualiza la mano, el estado y la interfaz.)
    """

    global estado, mensaje, puntajeJugador

    if estado != "jugador":
        return

    #Utiliza la función 'RepartirCarta' para jalar una carta de la baraja y esa carta se la agrega a la mano.
    carta = RepartirCarta(baraja)
    mano_jugador.append(carta)

    #Calcula el puntaje del jugador.
    puntajeJugador = 0
    NumeroDeAses = 0
    for carta in mano_jugador:
        NumeroDeAses = ContarAses(carta,NumeroDeAses)
        
        puntajeJugador = puntajeJugador + AgregarCarta(carta)
    puntajeJugador = GestionadorAs(puntajeJugador,NumeroDeAses)
        

    #Borra toda la mesa y la vuelve a generar con las cartas que se jalaron
    DibujarMesa()
    
    #   Determina si ya ganó el crupier o el jugador después de jalar carta; si alguno ganó, desactiva los botones dejando activo solo el de Nueva Partida.
    if puntajeJugador > 21:
        Plantarse()
        estado = "terminada"
        mensaje = "Te pasaste. Gana el Crupier."

    elif puntajeJugador == 21:
        Plantarse()
    else:
        estado_label.configure(text=f"Jalaste {carta[1]}. Tienes {puntajeJugador} puntos.")
    
   
######################################################################################################################################################################
#Función que gestiona la acción 'plantarse'.
######################################################################################################################################################################

def Plantarse() -> None:
    """
    Description:
        
        Termina el turno del jugador, ejecuta el turno del crupier,   
   
    Parameters:
    
        None 
    
    Raise:
        None 
        
    Returns:
    
        None:(Actualiza el estado y la interfaz.)
    """
    global estado, mensaje

    if estado != "jugador":
        return
   
    #Determina el puntaje
    puntajeJugador = 0
    NumeroDeAses = 0
    for carta in mano_jugador:
        NumeroDeAses = ContarAses(carta,NumeroDeAses)
        
        puntajeJugador = puntajeJugador + AgregarCarta(carta)
    puntajeJugador = GestionadorAs(puntajeJugador,NumeroDeAses)


    valcarta1 = AgregarCarta(mano_crupier[0])
    AsesCrupier = 0
    AsesCrupier = ContarAses(mano_crupier[0],AsesCrupier)
    puntajeCrupier = TurnoCrupier(valcarta1, puntajeJugador,AsesCrupier)
    print(puntajeJugador)
    
    

    #Determina si hay algún ganador
    if puntajeJugador > 21:
        mensaje = "Te pasaste. Gana el Crupier."
    elif puntajeCrupier > 21:
        mensaje = "El Crupier se pasó. ¡Ganaste!"
    elif puntajeJugador > puntajeCrupier:
        mensaje = "¡Ganaste!"
    elif puntajeJugador < puntajeCrupier:
        mensaje = "Gana el Crupier."
    else:
        mensaje = "Empate."

    #Si la partida termina se desactivan los botones.
    estado = "terminada"
    estado_label.configure(text=mensaje)
    jalar.configure(state="disabled")
    plantarse.configure(state="disabled")
    
    #Actualiza el mazo
    DibujarMesa()






##############################################################################################################################################################
#Función que gestiona el turno del crupier.
######################################################################################################################################################################

def TurnoCrupier(valcarta1: int, puntajejugador: int, Asinicial:int) -> int:
    """
    Description:
        
        Ejecuta el turno del crupier.  
   
    Parameters:
    
        Valcarta1(int): Valor de la carta destapada de la mano del crupier.
        puntajejugador(int): Puntaje que el jugador obtuvo en su turno.
        Asinicial(int): Si la carta destapada es un as.
    Raises:
        ValueError: Si valcarta1 es menor a 1 o mayor a 11, si puntajeJugador es menor a 4  o (Asinicial menor a cero o mayor a 1)
        TypeError: Si valcarta1 no es int, si puntajejugador no es int o si Asinicial no es int.
        
        
    Returns:
    
        None:(Actualiza el estado y la interfaz.)
    """
    if not isinstance(valcarta1,int):
        raise TypeError("La variable valcarta1 contiene un tipo de dato incompatible.")
    if not isinstance(puntajejugador,int):
        raise TypeError("La variable puntajejugador contiene un tipo de dato incompatible.")
    if not isinstance(Asinicial,int):
        raise TypeError("La variable Asinicial contiene un tipo de dato incompatible.")
    if valcarta1 > 11 or valcarta1 < 1:
        raise ValueError("El valor de la variable valcarta1 es inválido.")
    if puntajejugador < 4 :
        raise ValueError("El valor de la variable puntajejugador es inválido.")
    if Asinicial > 1 or Asinicial < 0:
        raise ValueError("El valor de la variable Asinicial es inválido.")
    
    
    AsesCrupier = Asinicial
    carta2 = mano_crupier[1]
    puntaje = valcarta1 + AgregarCarta(carta2)
    puntaje = GestionadorAs(puntaje,AsesCrupier)
    
    while (puntaje < 17 and puntaje != 21) and puntajejugador < 21  :
        cartaextra = RepartirCarta(baraja)
        mano_crupier.append(cartaextra)
        print(f'Ases: {AsesCrupier}')
        AsesCrupier = 0
        puntaje = 0
        for carta in mano_crupier:
         AsesCrupier = ContarAses(carta,AsesCrupier)
        
         puntaje = puntaje + AgregarCarta(carta)
         print(puntaje)
        puntaje = GestionadorAs(puntaje,AsesCrupier)
        print(puntaje)
    DibujarMesa()

    return puntaje







##############################################################################################################################################################################################################################################################################
#Configuración de los botones
##############################################################################################################################################################################################################################################################################

#Esto ordena los botones en la parte inferior del programa y los distribuye
contenedor = ctk.CTkFrame(ventana,fg_color="transparent")
contenedor.pack(side="bottom", fill="x", padx=45, pady=35)

# Función para crear botones
def crear_boton(texto, color, hover) -> None:
    """
    Description:
        
        Crea un botón con el estilo indicado dentro del contenedor de botones.
        
    Parameters:
    
        texto(str): Mensaje que va a tener el botón.
        color(str): Color del botón.
        hover(str): Color del resalte del botón.
    
    Raises:
    
        TypeError:  Cuando las variables ingresadas no son str.
 
    Returns:
    
        None:(Actualiza el estado y la interfaz.)
    """
    if not isinstance (texto,str):
        raise TypeError("El tipo de la variable texto es incompatible.")
    if not isinstance (color,str):
        raise TypeError("El tipo de la variable color es incompatible.")
    if not isinstance (hover,str):
        raise TypeError("El tipo de la variable hover es incompatible.")
    
    return ctk.CTkButton(contenedor,text=texto,width=200,height=55,corner_radius=16,font=("Georgia", 18, "bold"),fg_color=color,hover_color=hover,text_color="white",border_width=1,border_color="#D8B85A")
    

#Aquí utilicé la función que crea botones y le ingresé los parámetros que quería para cada botón.
nuevo_juego = crear_boton("Nuevo juego", "#B58A32", "#D0A747")

jalar = crear_boton("Jalar carta", "#126B48", "#18875B")

plantarse = crear_boton("Plantarse", "#126B48", "#18875B")

#El .pack sirve para mostrarlos en pantalla
nuevo_juego.pack(side="left", expand=True, padx=10)
jalar.pack(side="left", expand=True, padx=10)
plantarse.pack(side="left", expand=True, padx=10)


#Al darle click a los botones, mandará llamar a la función correspondiente.
nuevo_juego.configure(command=NuevaPartida)
jalar.configure(command=JalarCarta)
plantarse.configure(command=Plantarse)



# Inicia la partida al abrir la ventana
ventana.after(100, NuevaPartida())


#Comando para que al iniciar el programa no se cierre inmediatamente
ventana.mainloop()
