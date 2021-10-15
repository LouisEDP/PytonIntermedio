'''
modulo en el que se implementa el modelo de un Enemigo para simular 
diferentes ataques a un personaje.
atributos:
    tipo       --tipo de enemigo
    ataque     --ataque que realiza el enemigo
    energia    --HP del enemigo
    fuerza     --poder de ataque del enemigo
comportamientos
    atacar     --permite realizar el ataque especial al personaje
'''
MOMIA = 0
ZOMBI = 1
VAMPIRO = 2

tipos = [MOMIA,ZOMBI,VAMPIRO] # lista para poder crear de manera aleatoria a los enemgios

class Enemigo:
    def __init__(self, tipo='', ataque='', energia=5, fuerza=5):
        self._tipo = tipo
        self._ataque = ataque
        self._energia = energia
        self._fuerza = fuerza 

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, valor):
        self._tipo=valor
    @tipo.deleter
    def tipo(self):
        del self._tipo

    @property
    def ataque(self):
        return self._ataque
    @ataque.setter
    def ataque(self, valor):
        self._ataque=valor
    @ataque.deleter
    def ataque(self):
        del self._ataque

    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self, valor):
        self._energia=valor
    @energia.deleter
    def energia(self):
        del self._energia
    
    @property
    def fuerza(self):
        return self._fuerza
    @fuerza.setter
    def fuerza(self, valor):
        self._fuerza=valor
    @fuerza.deleter
    def fuerza(self):
        del self._fuerza
    
    def atacar(self):
        print(f'{self.tipo} ha atacado con {self.ataque}.')
        print(f'{self.tipo} ha cuasado {self.fuerza} de daño.')
    

class Momia(Enemigo):
    def __init__(self):
        super().__init__('Momia', 'Nesfa', 8, 12)
    

class Zombi(Enemigo):
    def __init__(self):
        super().__init__('Zombie', 'Fulacer', 4, 14)
    

class Vampiro(Enemigo):
    def __init__(self):
        super().__init__('Vampiro', 'estocada', 5, 10)
        self._recuperacion = 3

    @property
    def recuperacion(self):
        return self._recuperacion
    @recuperacion.setter
    def recuperacion(self, valor):
        self._recuperacion=valor
    @recuperacion.deleter
    def recuperacion(self):
        del self._recuperacion

    def atacar(self):
        super().atacar()
        print(f'{self.tipo} ha recuperado {self.recuperacion} de HP')
        self.energia += self.recuperacion