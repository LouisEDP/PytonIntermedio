class Persona:
    def __init__(self):
        self._edad = None

    @property
    def nombre(self):
        return self._nombre
 
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    @nombre.deleter
    def nombre(self):
        del self._nombre



    @property
    def edad(self):
        return self._edad
  
    @edad.setter
    def edad(self, valor):
        self._edad = valor
    
    @edad.deleter
    def edad(self):
        del self._edad
    
    def hablar(self, mensaje):
        print(f'{self.nombre}: {mensaje}')

    def comer(self, alimento):
        print(f'{self.nombre} esta comiendo {alimento}')


def main():
    persona_1 = Persona()
    persona_2 = Persona()

    persona_1.nombre = 'Louis'
    persona_1.edad = 24

    persona_2.nombre = 'Homero'
    persona_2.edad = 56

    persona_1.comer('Guisado')
    persona_2.comer('verga')

    print('Datos personas')
    print(f'Nombre {persona_1.nombre}')
    print(f'Edad: {persona_1.edad}')

    print('Datos personas 2')
    print(f'Nombre {persona_2.nombre}')
    print(f'Edad: {persona_2.edad}')

    persona_1.hablar(f'Kioña {persona_2.nombre}')
    persona_2.hablar(f'que paso {persona_1.nombre}')

if __name__=='__main__':
    main()
