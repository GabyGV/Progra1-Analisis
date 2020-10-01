#########################################################
#Creado por: Allison M y Gaby G       #                 #
#Fecha: 21/9/2020                     #  ANALISIS DE    #
#Ultima actuallizacion: 30/9/2020     #  ALGORITMOS     #
#Version: 3.8.2                       #                 #
#########################################################

###IMPORTACIONES###
import copy #para generar una copia del tablero

###CLASES###

class Color:
    rojo = 'red'
    azul = 'blue'
    verde = 'green'
    morado = 'magenta'
    amarillo = 'yellow'
    celeste = 'cyan'

class Figura:
    
    cuadrado = '■'
    circulo = '●'
    estrella = '★'
    triangulo = '▲'
    diamente = '◆'
    asterisco = '❈'

class Pieza:
    
    def _init_(self, color=None, forma=None):
        self.color = color
        self.forma = forma

    def toString(self):
        return '%s %s' % (self.color, self.forma)


class Tablero:
    
    def _init_(self):
        self.table = []
        self.tableAnterior = []
        self.jugadas = []
        self.ultimasJugadas=[]

    def reiniciarTablero(self):
        self.table = []
        self.jugadas = []

    def empezarTurno(self):
        self.jugadas = []
        self.tableAnterior = copy.deepcopy(self.table)

    def getJugadasValidas(self):
        jugadasValidas = []
        if not self.table:
            return [(1,1)]

        for fila in range(len(self.table)):
            for columna in range(len(self.table[fila])):
                if self.esJugadaValida(None, columna, fila): #pendiente programar funcion
                    jugadasValidas.append((columna, fila))

        return jugadasValidas
                    
    def getTablero(self):
        return self.table

    def getJugadas(self):
        return self.jugadas

    def jugar(jugar, pieza, col=1, fil=1):
        if len(self.table)==0:
            self.table = [[None]*3 for i in range(3)]
            col = 1
            fil = 1
        else:
            if not self.esJugadaValida(pieza, col, fil):
                print("Poner aqui una except")

        self.table[fil][col] = pieza
        self.jugadas.append((col,fil))
        self.validarVacios() #pendiente de programar

    def puntaje(self):
        if len(self.jugadas) == 0:
            return 0

        puntos = 0
        obtenidosHorizontales = []
        obtenidosVerticales = []

        for jugada in self.jugadas:
            col, fil = jugada

            minCol = col
            while minCol -1 >= 0 and self.table[fil][minCol -1] is not None:
                minCol -= 1

            maxCol = col
            while maxCol +1 < len(self.table[fila]) and self.table[fil][maxCol +1] is not None:
                maxCol += 1

            if minCol != maxCol:
                cuenta = 0
                for i in range(minCol, maxCol +1):
                    if (i, fil) not in obtenidosHorizontales:
                        puntos +=1
                        cuenta +=1
                        obtenidosHorizontales.append(i,fil)

                        if (col, fil) not in obtenidosHorizontales:
                            puntos +=1
                            cuenta +=1
                            obtenidosHorizontales.append((col, fil))

                    i +=1

                if cuenta == 6:
                    puntos +=6

            #repetir con filas#
            minFil = y
            while minFil -1 >= 0 and self.table[minFil -1][col] is not None:
                minFil -= 1

            maxFil = fil
            while maxFil +1 < len(self.table) and self.table[maxFil +1][col] is not None:
                maxFil += 1

            if minFil != maxFil:
                cuenta = 0
                for i in range(minFil, minFil +1):
                    if (col, i) not in obtenidosVerticales:
                        puntos +=1
                        cuenta +=1
                        obtenidosVerticales.append(col,i)

                        if (col, fil) not in obtenidosVerticales:
                            puntos +=1
                            cuenta +=1
                            obtenidosVerticales.append((col, fil))

                    i +=1

                if cuenta == 6:
                    puntos +=6

        return puntos

    def terminarTurno(self):
        self.ultimasJugadas = self.jugadas[:]
        self.jugadas = []
            
    def reiniciarTurno(self):
        self.table = copy.deepcopy(self.tableAnterior)
        self.jugadas = []

    def esJugadaValida(self, pieza, col, fil):
        if col < 0 or col >=len(self.table):
            return False
        if fil < 0 or fil >=len(self.table):
            return False
        if col == 0 and y==0:
            return False
        if col == 0 and fila ==len(self.table) -1:
            return False
        if col == len(self.table[0]) -1 and fil ==len(self.board) -1:
            return False
        if col == len(self.table[0]) -1 and fil == 0:
            return False
        if self.table[fil][col] is not None:
            return False
        campoCercano = []
        if fil -1 >=0:
            campoCercano.append((self.table[fil -1][col] is None))
        if fil +1 < len(self.table):
            campoCercano.append((self.table[fil +1][col] is None))
        if col -1 >=0:
            campoCercano.append((self.table[fil][col -1] is None))
        if col +1 < len(self.table[fil]):
            campoCercano.append((self.table[fil][col +1] is None))

        if all(campoCercano):
            return False

        juego = [(juegada[0], jugada[1]) for jugada in self.jugadas]
        if len(juego) > 0:
            validarHori = True
            validarVerti = True
            if len(juego) > 1:
                if juego[0][0] == juego[1][0]:
                    validarHori = False
                if juego[0][1] == juego[1][1]:
                    validarVerti = False

            enJugada = False
            if validarHori:
                valCol = col
                while valCol -1 >= 0 and self.table[fil][valCol -1] is not None:
                    valCol -= 1
                    if (valCol, fil) in juego:
                        enJugada = True

                valCol = col
                while valCol +1 < len(self.table[fil]) and self.table[fil][valCol +1] is not None:
                    valCol += 1
                    if (valCol, fil) in juego:
                        enJugada = True
                        
            if validarVerti:
                valFil = fil
                while valFil -1 >=0 and self.table[valFil -1][col] is not None:
                    valFil -= 1
                    if(col, valFil) in juego:
                        enJugada = True
                valFil = fil
                while valFil +1 <len(self.table) and self.table[valFil +1][col] is not None:
                    valFil += 1
                    if(col, valFil) in juego:
                        enJugada = True

            if not enJugada:
                return False

            if pieza is None:
                return True

            lugar = [pieza]
            valCol = col +1
            while valCol < len(self.table[0]) and self.table[fil][valCol] is not None:
                lugar.append(self.table[fil][valCol])
                valCol +=1

            valCol = col -1
            while valCol >=0 and self.table[fil][valCol] is not None:
                lugar.append(self.table[fil][valCol])
                valCol -=1

            if not self.esFilaValida(lugar): #pendiente de programar
                return False

            lugar = [pieza]
            valFil = fil +1
            while valFil < len(self.table) and self.table[valFil][col] is not None:
                lugar.append(self.table[valFil][col])
                valFil +=1

            valFil = fil -1
            while valFil >=0 and self.table[valFil][col] is not None:
                lugar.append(self.table[valFil][col])
                valFil -= 1

            if not self.esFilaValida(lugar):
                return False

            return True

    def esFilaValida(self, fila):
        if len(fila) == 1:
            return True
        if all(fila[i].color == fila[0].color for i in range(len(fila))):
            figuras = []
            for i in range(len(fila)):
                if fila[i].forma in figuras:
                    return False
                figuras.append(fila[i].forma)

        elif all (fila[i].forma == fila[0].forma for i in range(len(fila))):
            colores = []
            for i in range(len(fila)):
                if fila[i].color in colores:
                    return False
                colores.append(fila[i].color)
        else:
            return False

        return True

    def validarVacios(self):
        if any(self.table[0][i] is not None for i in range(len(self.table[0]))):
              self.table.insert(0, [None] * (len(self.table[0])))
              self.jugadas = [(jugada[0], jugada[1]+1) for jugada in self.jugadas]
              self.ultimasJugadas = [(jugada[0], jugada[1]+1) for jugada in self.ultimasJugadas]

        fondo = len(self.table) -1
        if any(self.table[fondo][i] is not None for i in range(len(self.table[0]))):
            self.table += [[None] * (len(self.table[0]))]

        if any(self.table[i][0] is not None for i in range(len(self.table))):
            for i in range(len(self.table)):
                self._table[i].insert(0, None)
            self.jugadas = [(jugada[0] + 1, jugada[1]) for jugada in self.jugadas]
            self.ultimasJugadas = [(jugada[0] + 1, jugada[1]) for jugada in self.ultimasJugadas]
            
        derecha = len(self.table[0]) - 1
        if any(self._table[i][derecha] is not None for i in range(len(self.table))):
            for i in range(len(self.table)):
                self.table[i] += [None]


###FUNCIONES###
def generarBolsa():
    bolsaDeFichas = []
    figuras = [Figura.circulo, Figura.cuadrado, Figura.triangulo, Figura.diamante, Figura.estrella, Figura.asterisco]
    colores = [Color.rojo, Color.azul, Color.amarillo, Color.celeste, Color.morado, Color.verde]

    for i in range(3):
        for j in range(len(colores)):
            for k in range(len(figuras)):
                bolsaDeFichas.append(Pieza(color=colores[j], forma=figuras[k]))
