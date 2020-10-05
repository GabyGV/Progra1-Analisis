class COLORES:
    ROJO = 'red'
    AMARILLO = 'yellow'
    VERDE = 'green'
    CYAN = 'cyan'
    MAGENTA = 'magenta'
    AZUL = 'blue'


class FORMAS:
    TRINGULO = '▲'
    DIAMANTE = '◆'
    CUADRADO = '■'
    CIRCULO = '●'
    ESTRELLA = '★'
    SPARKLE = '❈'


class Pieza:
    def __init__(self, color=None, forma=None):
        self.color = color
        self.forma = forma

    def __str__(self):
        return '%s %s' % (self.color, self.forma)

    def __repr__(self):
        return self.__str__()