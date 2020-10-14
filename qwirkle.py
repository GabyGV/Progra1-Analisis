#IMPORTACIONES
from Tablero import Tablero, Pieza, FORMAS, COLORES
from jugador import Jugador
from bots import bot_basico, bot_mejorado


class QwirkleGame:
    def __init__(self):
        self.bolsa_de_fichas = []
        self._jugadores = []
        self._tablero = []

    def main(self, jugadores):

        self._tablero = Tablero()
        self._generar_nueva_bolsa_de_fichas()

        numero_de_jugador = 1
        for jugador in jugadores:
            if jugador == 'bot_basico':
                self._jugadores.append(bot_basico('Jugador %i' % numero_de_jugador))
            elif jugador == 'bot_mejorado':
                self._jugadores.append(bot_mejorado('Jugador %i' % numero_de_jugador))
            elif jugador == 'humano':
                self._jugadores.append(Jugador('Jugador %i' % numero_de_jugador))
            else:
                raise ValueError('%s no es un tipo de jugador válido' % jugador)
            numero_de_jugador += 1

        score_message = (-1, 0)
        jugador_actual = 0
        while True:
            print('\n' * 30)
            print('====================QWIRKLE====================\n')

            print('  Puntaje:')
            for i in range(len(self._jugadores)):
                message = '    %s - %i' % (self._jugadores[i].nombre(), self._jugadores[i].score())
                if score_message[0] == i:
                    message += ' +%i' % score_message[1]
                print(message)
            print('\n  Es el turno de:  %s\n' % self._jugadores[jugador_actual].nombre())

            self._tablero.imprimir_tablero(show_valid_placements=False)
            self._jugadores[jugador_actual].elegir_fichas(self._bolsa_de_fichas)
            self._tablero.empezar_turno()
            self._jugadores[jugador_actual].jugar_turno(self._tablero)

            score = self._tablero.score()
            self._jugadores[jugador_actual].agregar_puntos(score)

            score_message = (jugador_actual, score)
            self._tablero.terminar_turno()

            if score == 0:
                print('  %s está cambiando fichas...' % self._jugadores[jugador_actual].nombre())
                self._bolsa_de_fichas += self._jugadores[jugador_actual].get_fichas()
                self._jugadores[jugador_actual].clear_fichas()

            self._jugadores[jugador_actual].elegir_fichas(self._bolsa_de_fichas)

            if self._jugadores[jugador_actual].sin_fichas():
                break

            jugador_actual += 1
            if jugador_actual >= len(self._jugadores):
                jugador_actual = 0

        winning_player = max(self._jugadores, key=lambda p: p.score())

        print('\n  Puntaje Final:')
        for i in range(len(self._jugadores)):
            message = '    %s - %i' % (self._jugadores[i].nombre(), self._jugadores[i].score())
            print(message)

        print('\n  %s ¡Ha ganado!\n' % winning_player.nombre())

    def _generar_nueva_bolsa_de_fichas(self):
        self._bolsa_de_fichas = []

        formas = [
            FORMAS.CIRCULO,
            FORMAS.DIAMANTE,
            FORMAS.SPARKLE,
            FORMAS.CUADRADO,
            FORMAS.ESTRELLA,
            FORMAS.TRIANGULO
        ]

        colores = [
            COLORES.AZUL,
            COLORES.CYAN,
            COLORES.VERDE,
            COLORES.MAGENTA,
            COLORES.ROJO,
            COLORES.AMARILLO
        ]

        for i in range(3): #PARA GENERAR TRES JUEGOS DE FICHAS
            for c in range(len(colores)): #POR CADA COLOR
                for s in range(len(formas)): #POR CADA FORMA
                    self._bolsa_de_fichas.append(Pieza(color=colores[c], forma=formas[s])) #SE AGREGA UNA PIEZA A LA BOLSA DE FICHAS
