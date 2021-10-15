'''
pelicula.py
Modulo de una pelicula
Atributos:
    titulo      --titulo de la pelicula.
    director    --director de la pelicula.
    anio        --año de estreno.
    direcion    --direcion en minutos de la pelicula.
'''

class Pelicula:
    def __init__(self, titulo='', director='', anio=None, duracion=None):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.duracion = duracion

    
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor
    @titulo.deleter
    def titulo(self):
        del self._titulo

    @property
    def director(self):
        return self._director
    @director.setter
    def director(self, valor):
        self._director = valor
    @director.deleter
    def director(self):
        del self._director

    @property
    def anio(self):
        return self._anio
    @anio.setter
    def anio(self, valor):
        self._anio = valor
    @anio.deleter
    def anio(self):
        del self._anio
    
    @property
    def duracion(self):
        return self._duracion
    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor
    @duracion.deleter
    def duracion(self):
        del self._duracion

    def __str__(self):
        ESPACIO = 10
        return f'''{"Titulo:" : <{ESPACIO}}{self._titulo}
{"Director:" : <{ESPACIO}}{self.director}
{"Año:" : <{ESPACIO}}{self.anio}
{"Duracion:" : <{ESPACIO}}{self.duracion} min'''
     #lower than
    def __lt__(self, other):
        return self.titulo < other.titulo
     #equal
    def __eq__(self, other):
        return self.director == other.director and self.anio == other.anio
     #lower or equal
    def __le__(self, other):
        return self < other or self == other