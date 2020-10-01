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
from tablero import InvalidPlayException


class bot_basico(Player): #Falta programar Player
    def jugar_turno(self, tablero):
        starts_validos = tablero.jugadas_posibles() #verifica cuales son las jugadas disponibles

        jugadas = [] #almacenará las jugadas posibles con sus puntajes
        for (fila, columna) in starts_validos: #por cada jugada valida
            fichas = self._fichas.copy() #copia las fichas que tiene Player

            for i in range(len(fichas)): #por cada ficha 
                try:
                    tablero.jugar(fichas[i], x=fila, y=columna) #manda a jugar a la ficha en la posición disponible
                    jugadas.append({ 
                        'jugadas': [(fila, columna, fichas[i])],
                        'score': tablero.score() #agrega a la lista la jugada y el puntaje obtenido
                    })
                    fichas_restantes.pop(i) #elimina la ficha que ya se usó
                    break
                except InvalidPlayException: #si la jugada no es valida, tira una excepción | falta programar
                    pass

            tablero.reiniciar_turno() #deja el tablero como antes

        if len(jugadas) == 0: 
            return

        mejor_jugada = max(jugadas, key=lambda p: p['score']) #saca los puntajes más altos obtenidos en las jugadas usando la llave score

        for (fila, columna, ficha) in mejor_jugada['jugadas']: #por cada una de las mejores jugadas
            tablero.jugar(ficha, fila, columna) #realiza la jugada en el tablero
            self._fichas.pop(self._fichas.index(ficha))  #elimina la ficha usada
