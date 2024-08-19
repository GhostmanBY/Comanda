class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def cambio_nombre(self, nombre):
        self.__nombre = nombre

    def presentarse(self):
        print(f"Hola, me llamo {self.__nombre} y tengo {self.__edad} años.")

persona = Persona("Juan", 25)
persona.presentarse()
persona.cambio_nombre("Jose")
persona.presentarse()