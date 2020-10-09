from random import Random
from termcolor import colored
from Tablero import InvalidPlayException


class Jugador:
    def __init__(self, nombre='Jugador Desconocido'):
        self._fichas = []
        self._score = 0
        self._nombre = nombre

    def ejegir_fichas(self, bolsa_de_fichas):
        rnd = Random()
        while len(self._fichas) < 6 and len(bolsa_de_fichas) > 0: #mientras el jugador tenga menos de 6 fichas y la bolsa de fichas no esté vacía
            i = rnd.randint(0, len(bolsa_de_fichas) - 1) #elige un número random entre 0 y el largo de la bolsa de fichas para sacar una ficha

            self._fichas.append(bolsa_de_fichas.pop(i)) #se elimina de la bolsa de fichas la elegida y al mismo tiempo se agrega a las fichas del jugador

    def jugar_turno(self, tablero):
        fichas = self._fichas.copy()
        while True:
            self.print_fichas(fichas)
            print('  Opciones')
            print('   "r"  para reiniciar el tablero')
            print('   "t# @#" para colocar una ficha, donde # es el número de la ficha, @ es la letra de la coordenada y  # es el número de la coordenada')
            print('   "f" para terminar el turno\n')
            eleccion = input('--> ')
            print('\n')

            if len(eleccion) == 0:
                continue

            if eleccion == 'r':
                tablero.reiniciar_turno()
                fichas = self._fichas.copy()
                tablero.imprimir_tablero()
                continue

            if eleccion == 'f':
                break

            if eleccion[0] != 't':
                continue

            try:
                indice_ficha = int(eleccion[1]) - 1
            except ValueError:
                print(colored('¡Ficha inválida!', 'red'))
                continue

            if indice_ficha >= len(fichas):
                continue

            x, y = tablero.coord_to_position(eleccion[3:].upper())

            try:
                tablero.jugar(fichas[indice_ficha], x, y)
                fichas.pop(indice_ficha)
            except InvalidPlayException:
                print(colored('¡Jugada inválida!', 'red'))

            tablero.imprimir_tablero()

        self._fichas = fichas.copy()

    @staticmethod
    def print_fichas(fichas):
        fichas_output = ''
        for ficha in fichas:
            fichas_output += colored(ficha.forma, ficha.color) + ' '
        print('\n  Sus fichas: %s' % fichas_output)
        print('              1 2 3 4 5 6\n')

    def score(self):
        return self._score

    def agregar_puntos(self, puntos):
        self._score += puntos

    def sin_fichas(self):
        return len(self._fichas) == 0

    def nombre(self):
        return self._nombre

    def get_fichas(self):
        return self._fichas

    def clear_fichas(self):
        self._fichas = []

