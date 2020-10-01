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
        return '%s %s' % (self.color, self.figura)


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
            self.table() = [[None]*3 for i in range(3)]
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
            
        

###FUNCIONES###
