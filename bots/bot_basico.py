####################################################
# Creado por: Gabriela Gutiérrez y Allison Montero #
# Fecha: 21/09/2020 7:00pm                         #
# Actualizado: XX/09/2020 7:00pm                   #
# Versión: 1.1                                     #
# Nombre: bot-basico                               #
####################################################
#                 TAREA PROGRAMADA 1               #
####################################################

import copy
from jugador import Jugador
from Tablero import InvalidPlayException #podría ser aquí

jugadas = [] #almacenará las jugadas posibles con sus puntajes


class bot_basico(Jugador):
    def jugar_turno(self, tablero):
        starts_validos = tablero.jugadas_posibles() #verifica cuales son las jugadas disponibles
        fichas = self._fichas.copy() #copia las fichas que tiene Player

        #jugadas = [] 
        bot_backtraking(tablero, starts_validos, fichas, 0)

        tablero.reiniciar_turno() #deja el tablero como antes

        if len(jugadas) == 0: 
            return

        mejor_jugada = max(jugadas, key=lambda p: p['score']) #saca los puntajes más altos obtenidos en las jugadas usando la llave score

        for (fila, columna, ficha) in mejor_jugada['jugadas']: #por cada una de las mejores jugadas
            tablero.jugar(ficha, fila, columna) #realiza la jugada en el tablero
            self._fichas.pop(self._fichas.index(ficha))  #elimina la ficha usada

#Backtraking
def bot_backtraking(tablero, starts_validos, fichas, i):

    if i >= len(fichas): #condición de salida
        return 

    for (fila, columna) in starts_validos:
        try:
            tablero.jugar(fichas[i], fila=fila, columna=columna) #manda a jugar a la ficha en la posición disponible
            jugadas.append({ 
            'jugadas': [(fila, columna, fichas[i])],
            'score': tablero.score() #agrega a la lista la jugada y el puntaje obtenido #antes de esto puede estar la condición de poda
            })
        except InvalidPlayException: #si la jugada no es valida, tira una excepción 
                pass

        bot_backtraking(tablero, starts_validos, fichas, i+1)
    return 