class Hero:
    # funciona como un constructor
    def __init__(self):
        # No necesito de getters y setters para acceder a los atributos :)
        self.nombre = ''
        self.poder = ''

    def saludar(self):
        print(f'hola soy {self.nombre} y mi super poder es {self.poder}')


heroe = Hero()
heroe.nombre = 'PETER PARKER'
heroe.poder = 'SENTIDO ARACNIDO'
heroe.saludar()


class Hero2:

    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def saludar(self):
        print(f'hola soy {self.nombre} y mi super poder es {self.poder}')


# puedo colocar en el constructor parametros y enviarlos en la instancia de la clase.
wolverine = Hero2('LOGAN', 'REGENERACIÓN')
wolverine.saludar()


## Para la herencia entre clases se pasan como arg en la clase sepadados por coma
# ex. class ClaseA(ClaseB, ClaseC): pass

class Villano(Hero2):
    def saludo(self):
        print(f'soy {self.nombre} y mi poder es {self.poder}')


villano = Villano('JOKER', 'MI SONRISA xd')
villano.saludo()
