##################################
#       ARCHIVO PRINCIPAL        #
#   ESTE ES EL QUE DEBE CORRER   #
##################################

#IMPORTACIONES
from qwirkle import QwirkleGame

jugadores = [] #LISTA PARA LOS 2 JUGADORES

while len(jugadores) < 2: #MENU PARA ESCOGER A LOS JUGADORES
    print("\n")
    print ("1. Humano")
    print("2. Bot básico")
    print("3. Bot mejorado\n")

    respuesta = int(input("Ingrese el número de jugador: "))
    if(respuesta == 1):
        jugadores.append("humano")
    elif(respuesta == 2):
        jugadores.append("bot_basico")
    elif(respuesta == 3):
        jugadores.append("bot_mejorado")
    else:
        print("Respuesta invalida")

juego = QwirkleGame() #CREA EL JUEGO
juego.main(jugadores) #INICIA EL JUEGO