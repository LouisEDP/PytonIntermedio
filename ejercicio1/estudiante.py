from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre='', edad=None, numero=None, promedio=None):
        super().__init__(nombre, edad)
        self._numero = numero
        self._promedio = promedio

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, valor):
        self._numero = valor
    @numero.deleter
    def numero(self):
        del self._numero

    @property
    def promedio(self):
        return self._promedio
    @promedio.setter
    def promedio(self, valor):
        if valor < 10:
            self._promedio = None
        else:
            self._promedio = valor
    @promedio.deleter
    def promedio(self):
        del self._promedio
    
    def estudiar(self, materia):
        print(f'{self.nombre} esta estudiando {materia}')

    def __str__(self):
        return f'''{super().__str__()}
Promedio: {self.promedio}
ID estudiante: {self.numero}'''
