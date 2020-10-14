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
from termcolor import colored

#jugadas = [] #almacenará las jugadas posibles con sus puntajes


class bot_mejorado(Jugador):
    def jugar_turno(self, tablero):
        starts_validos = tablero.jugadas_posibles() #verifica cuales son las jugadas disponibles
        fichas = self._fichas.copy() #copia las fichas que tiene Player
        print_fichas(fichas)

        global jugadas 
        jugadas = []
        bot_backtraking(tablero, starts_validos, fichas, 0)

        tablero.reiniciar_turno() #deja el tablero como antes

        if len(jugadas) == 0: 
            return

        mejor_jugada = max(jugadas, key=lambda p: p['score']) #saca los puntajes más altos obtenidos en las jugadas usando la llave score

        for (fila, columna, ficha) in mejor_jugada['jugadas']: #por cada una de las mejores jugadas
            try:
                tablero.jugar(ficha, fila, columna) #realiza la jugada en el tablero
                self._fichas.pop(self._fichas.index(ficha))  #elimina la ficha usada
            except InvalidPlayException:
                pass

#Backtraking
def bot_backtraking(tablero, starts_validos, fichas, i):

    if i >= len(fichas): #condición de salida
        return 

    for (fila, columna) in starts_validos:
        #fichaJugada = False
        try:
            tablero.jugar(fichas[i], fila, columna) #manda a jugar a la ficha en la posición disponible
            if(tablero.score() != 5):
                jugadas.append({ 
                'jugadas': [(fila, columna, fichas[i])],
                'score': tablero.score() #agrega a la lista la jugada y el puntaje obtenido #antes de esto puede estar la condición de poda
                })
                #fichaJugada = True
                #fichasRestantes = fichas.copy()
                #fichasRestantes.pop(i)
            if tablero.score() == 12:
                return
        except InvalidPlayException: #si la jugada no es valida, tira una excepción 
                pass
        """ ahi mas o menos intente ponerlo
        while fichaJugada:
                    fichaJugada = False
                    for (nx, ny) in tablero.jugadas_posibles():
                        for j in range(len(tiles_remaining)):
                            try:
                                tablero.jugar(tiles_remaining[j], x=nx, y=ny)
                                plays[-1]['plays'].append((nx, ny, tiles_remaining[j]))
                                plays[-1]['score'] = tablero.score()
                                tiles_remaining.pop(j)
                                fichaJugada = True
                                break
                            except InvalidPlayException:
                                pass"""

        bot_backtraking(tablero, starts_validos, fichas, i+1)
    return 

def print_fichas(fichas):
    fichas_output = ''
    for ficha in fichas:
        fichas_output += colored(ficha.forma, ficha.color) + ' '
    print('\n  Las fichas: %s' % fichas_output)
    print('              1 2 3 4 5 6\n')