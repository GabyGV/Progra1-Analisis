####################################################
# Creado por: Gabriela Gutiérrez y Allison Montero #
# Fecha: 21/09/2020                                #
# Actualizado: XX/09/2020                          #
# Versión: 1.1                                     #
#                   TABLERO                        #
####################################################
#                 TAREA PROGRAMADA 1               #
####################################################

#Librerías
from termcolor import colored
import copy
from Tablero.excepciones import InvalidPlayException

class Tablero:

    def __init__(self):
        self._tablero = []
        self._tablero_anterior = []
        self._jugadas = []
        self._ultimas_jugadas = []

    def reiniciar_Tablero(self):
        #Limpia el tablero actual
        self._tablero = []
        self._jugadas = []

    def empezar_turno(self):
        #Empieza un nuevo turno para el siguiente jugador
        self._jugadas = []
        self._tablero_anterior = copy.deepcopy(self._tablero)

    def jugadas_posibles(self):
        #Devuelve las jugadas posibles
        jugadas_posibles = []

        if not self._tablero: #si la partida es nueva crea un tablero nuevo
            return [(1, 1)]

        for columna in range(len(self._tablero)): #recorre el tablero
            for fila in range(len(self._tablero[columna])):
                if self.la_jugada_es_valida(None, fila, columna): #verifica que el espacio esté disponible
                    jugadas_posibles.append((fila, columna)) #lo agrega a la lista
        return jugadas_posibles #devuelve la lista con las jugadas

    def get_tablero(self): 
        #Devuelve el tablero con los movimientos actuales
        return self._tablero

    def get_jugadas(self):
        return self._jugadas

    def jugar(self, ficha, fila=1, columna=1):
        #Coloca la ficha en el tablero
        if len(self._tablero) == 0: #si el tablero es nuevo y no hay jugadas
            self._tablero = [[None] * 3 for i in range(3)] #agranda el tablero
            #colocará la ficha en la posición 1,1
            fila = 1 
            columna = 1
        else:
            if not self.la_jugada_es_valida(ficha, fila, columna): #si la jugada no es válida, devuelve una excepción
                raise InvalidPlayException

        self._tablero[columna][fila] = ficha #coloca la ficha en el tablero
        self._jugadas.append((fila, columna)) #agrega la jugada a la lista de jugadas
        self._espaciar_tablero()


    def score(self):
        """Devuelve el score del turno actual"""
        if len(self._jugadas) == 0:
            return 0

        score = 0
        puntaje_horizontal = []
        puntaje_vertical = []

        for jugada in self._jugadas:
            fila, columna = jugada

            min_fila = fila
            while min_fila - 1 >= 0 and self._tablero[columna][min_fila - 1] is not None:
                min_fila -= 1

            max_fila = fila
            while max_fila + 1 < len(self._tablero[columna]) and self._tablero[columna][max_fila + 1] is not None:
                max_fila += 1

            if min_fila != max_fila:
                qwirkle_count = 0
                for t_fila in range(min_fila, max_fila + 1):
                    if (t_fila, columna) not in puntaje_horizontal:
                        score += 1
                        qwirkle_count += 1
                        puntaje_horizontal.append((t_fila, columna))

                        if (fila, columna) not in puntaje_horizontal:
                            score += 1
                            qwirkle_count += 1
                            puntaje_horizontal.append((fila, columna))
                    t_fila += 1

                if qwirkle_count == 6:
                    score += 6

            min_columna = columna
            while min_columna - 1 >= 0 and self._tablero[min_columna - 1][fila] is not None:
                min_columna -= 1

            max_columna = columna
            while max_columna + 1 < len(self._tablero) and self._tablero[max_columna + 1][fila] is not None:
                max_columna += 1

            if min_columna != max_columna:
                qwirkle_count = 0
                for t_columna in range(min_columna, max_columna + 1):
                    if (fila, t_columna) not in puntaje_vertical:
                        score += 1
                        qwirkle_count += 1
                        puntaje_vertical.append((fila, t_columna))

                        if (fila, columna) not in puntaje_vertical:
                            score += 1
                            qwirkle_count += 1
                            puntaje_vertical.append((fila, columna))
                    t_columna += 1

                if qwirkle_count == 6:
                    score += 6

        return score


    def terminar_turno(self):
        #finaliza el turno actual
        self._ultimas_jugadas = self._jugadas[:]
        self._jugadas = []


    def reiniciar_turno(self):
        #Reinicia el tablero y lo deja de la forma en la que estaba antes de la jugada actual
        self._tablero = copy.deepcopy(self._tablero_anterior)
        self._jugadas = []

    def imprimir_tablero(self, show_valid_placements=True):
        if len(self._tablero) == 0:
            print('  A')
            print('01', colored('■', 'white'))
            return

        jugadas_posibles = self.jugadas_posibles()
        lineas = []
        for columna in range(len(self._tablero)):
            linea = ''
            for fila in range(len(self._tablero[columna])):
                if self._tablero[columna][fila] is not None:
                    if (fila, columna) in self._ultimas_jugadas:
                        linea += colored(self._tablero[columna][fila].forma + ' ', self._tablero[columna][fila].color, 'on_white')
                    else:
                        linea += colored(self._tablero[columna][fila].forma + ' ', self._tablero[columna][fila].color)
                elif (fila, columna) in jugadas_posibles and show_valid_placements:
                    linea += colored('☐', 'white') + ' '
                else:
                    linea += '  '

            lineas.append(linea)

        # add in the top coord line
        linea = ''.join([chr(65 + i) + ' ' for i in range(len(self._tablero[0]))])
        lineas.insert(0, linea)
        lineas.append(linea)

        for i in range(0, len(lineas)):
            i_display = str(i).zfill(2) if 0 < i < len(lineas) - 1 else '  '
            print(i_display, lineas[i], i_display)

    @staticmethod
    def coord_to_position(coord):
        x_coord = ord(coord[0]) - 65
        y_coord = int(coord[1:]) - 1

        return x_coord, y_coord

    def la_jugada_es_valida(self, ficha, fila, columna):
        """Valida que el movimiento en el tablero no sea en las esquinas, no reemplace otra ficha, que sea adyacente 
        a otra ficha del tablero y sea valido en la columna y fila elegidas"""

        # Revisa que la posición no sea una esquina y esté dentro del tablero
        if fila < 0 or fila >= len(self._tablero[0]): #limites laterales
            return False
        if columna < 0 or columna >= len(self._tablero): #limites superior e inferior
            return False
        if fila == 0 and columna == 0: #esquina superior izquierda
            return False
        if fila == 0 and columna == len(self._tablero) - 1: #esquina superior derecha
            return False
        if fila == len(self._tablero[0]) - 1 and columna == len(self._tablero) - 1: #esquina inferior derecha
            return False
        if fila == len(self._tablero[0]) - 1 and columna == 0: #esquina inferior izquierda
            return False

        # Revisa que no haya una ficha en la posición solicitada
        if self._tablero[columna][fila] is not None:
            return False

        # Revisa que la posición tiene al menos un lugar adyacente
        adjacent_checks = []
        if columna - 1 >= 0: #hacia la derecha |  mayor a 0 para que esté dentro del tablero
            adjacent_checks.append((self._tablero[columna - 1][fila] is None)) #verifica si está vacío
        if columna + 1 < len(self._tablero): #hacia la derecha | menor al len para que esté dentro del tablero
            adjacent_checks.append((self._tablero[columna + 1][fila] is None)) #verifica si está vacío
        if fila - 1 >= 0: #hacia arriba
            adjacent_checks.append((self._tablero[columna][fila - 1] is None)) 
        if fila + 1 < len(self._tablero[columna]): #hacia abajo
            adjacent_checks.append((self._tablero[columna][fila + 1] is None)) 

        if all(adjacent_checks):
            return False

        # Revisa que la jugada conecta con una jugada adyacente
        jugadas = [(jugada[0], jugada[1]) for jugada in self._jugadas]
        if len(jugadas) > 0:
            check_horizontal = True
            check_vertical = True
            if len(jugadas) > 1: #revisa que haya al menos una jugada
                if jugadas[0][0] == jugadas[1][0]:
                    check_horizontal = False
                if jugadas[0][1] == jugadas[1][1]:
                    check_vertical = False

            in_plays = False

            if check_horizontal:
                t_fila = fila
                while t_fila - 1 >= 0 and self._tablero[columna][t_fila - 1] is not None:
                    t_fila -= 1
                    if (t_fila, columna) in jugadas:
                        in_plays = True

                t_fila = fila
                while t_fila + 1 < len(self._tablero[columna]) and self._tablero[columna][t_fila + 1] is not None:
                    t_fila += 1
                    if (t_fila, columna) in jugadas:
                        in_plays = True

            if check_vertical:
                t_columna = columna
                while t_columna - 1 >= 0 and self._tablero[t_columna - 1][fila] is not None:
                    t_columna -= 1
                    if (fila, t_columna) in jugadas:
                        in_plays = True

                t_columna = columna
                while t_columna + 1 < len(self._tablero) and self._tablero[t_columna + 1][fila] is not None:
                    t_columna += 1
                    if (fila, t_columna) in jugadas:
                        in_plays = True

            if not in_plays:
                return False

        # No revisa el color y la forma de la ficha si no hay ninguna ficha 
        if ficha is None:
            return True

        # Verifica todas las fichas adyacentes de forma horizontal
        row = [ficha]
        t_fila = fila + 1
        while t_fila < len(self._tablero[0]) and self._tablero[columna][t_fila] is not None: #revisa todas las fichas que hay a la derecha  posición 
            row.append(self._tablero[columna][t_fila]) #agrega las fichas a la lista
            t_fila += 1 

        t_fila = fila - 1
        while t_fila >= 0 and self._tablero[columna][t_fila] is not None: #revisa todas las fichas que hay a izquierda de la posición
            row.append(self._tablero[columna][t_fila]) #agrega las fichas a la lista
            t_fila -= 1

        if not self._is_row_valid(row): #la funcion verifica los colores y formas de toda la hilera
            return False

        # Verifica todas las fichas adyacentes de forma vertical
        row = [ficha]
        t_columna = columna + 1
        while t_columna < len(self._tablero) and self._tablero[t_columna][fila] is not None:  ##revisa todas las fichas que hay a abajo de la posición
            row.append(self._tablero[t_columna][fila])
            t_columna += 1

        t_columna = columna - 1
        while t_columna >= 0 and self._tablero[t_columna][fila] is not None: #revisa todas las fichas que hay a arriba de la posición
            row.append(self._tablero[t_columna][fila]) #agrega las fichas a la lista
            t_columna -= 1

        if not self._is_row_valid(row): #la funcion verifica los colores y formas de toda la hilera
            return False

        return True

    def _is_row_valid(self, row):
        """Si todos los colores son iguales, revisa que cada forma aparezca a lo mucho una vez.
           Si todas las formas son iguales, revisa que cada color aparece a lo muco una sola vez.
           Si lo anterior no se cumple, la hilera es inválida"""

        if len(row) == 1: #si la hilera solo contiene la ficha nueva, la hilera es válida
            return True

        if all(row[i].color == row[0].color for i in range(len(row))): #verifica si el color de todas las fichas es el mismo
            formas = [] 
            for i in range(len(row)): #por cada ficha
                if row[i].forma in formas: #si la ficha ya se encuentra en la lista de formas
                    return False #la hilera es inválida
                formas.append(row[i].forma) # si no, agrega la forma al lista de formas

        elif all(row[i].forma == row[0].forma for i in range(len(row))): #verifica si la forma de todas las fichas es la misma
            colors = []
            for i in range(len(row)): #por cada ficha
                if row[i].color in colors: #si el color ya se encuentra en la lista de colores 
                    return False #la hilera es inválida
                colors.append(row[i].color) #si no, agrega el color a la lista de colores

        else: #si ninguna de las condiciones anteriores se cumple
            return False #la hilera es inválida

        return True

    def _espaciar_tablero(self):
        """Se asegura de que hay un bloque de espacios vacios alrededor de la jugada, actualiza las jugadas"""

        # Revisa el bloque superior
        if any(self._tablero[0][i] is not None for i in range(len(self._tablero[0]))):
            self._tablero.insert(0, [None] * (len(self._tablero[0])))
            self._jugadas = [(play[0], play[1]+1) for play in self._jugadas]
            self._ultimas_jugadas = [(play[0], play[1]+1) for play in self._ultimas_jugadas]

        # Revisa el bloque inferior
        bottom = len(self._tablero) - 1
        if any(self._tablero[bottom][i] is not None for i in range(len(self._tablero[0]))):
            self._tablero += [[None] * (len(self._tablero[0]))]

        # Revisa el bloque izquierdo
        if any(self._tablero[i][0] is not None for i in range(len(self._tablero))):
            for i in range(len(self._tablero)):
                self._tablero[i].insert(0, None)
            self._jugadas = [(play[0] + 1, play[1]) for play in self._jugadas]
            self._ultimas_jugadas = [(play[0] + 1, play[1]) for play in self._ultimas_jugadas]

        # Right padding
        right = len(self._tablero[0]) - 1
        if any(self._tablero[i][right] is not None for i in range(len(self._tablero))):
            for i in range(len(self._tablero)):
                self._tablero[i] += [None]

