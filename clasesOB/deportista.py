'''
derportista.py
modelo de un deportista que hereda de la clase perosa.py
Atributos:
    deporte --Deporte que practica
comportamientos:
    entrenamiento  --entrena el deporte asignado
    '''


from persona import Humano


class Deportista(Humano):
    def __init__(self, nombre='', edad=None, deporte=''):
        super().__init__(nombre, edad)# para ahorrar codigo y no tener que defiir nombre y edad de nuevo
        self._deporte = deporte

    @property 
    def deporte(self):
        return self._deporte
    @deporte.setter
    def deporte(self, valor):
        self._deporte = valor
    @deporte.deleter
    def deporte(self):
        del self._deporte

    def entrenar(self):
        print(f'{self.nombre} esta entrenando {self.deporte}')

    def __str__(self):
        return f'''{super().__str__()}
Deporte: {self.deporte}'''