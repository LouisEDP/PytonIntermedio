
class Figura:
    def __init__(self):
        self._lados = None

    @property #getter: regresa un valor asociado a la cangidad de lados
    def lados(self):
        return self._lados
    
    @lados.setter #sett permite asignar valor a lapropiedad o atribulo lados
    def lados(self, valor):
        self._lados = valor
            

    @lados.deleter # elimina la propiedad
    def lados(self):
        del self._lados

def main():
    circulo = Figura()
    triangulo = Figura()

    circulo.lados = 1
    triangulo.lados = 3

    print(f'El circulo tiene {circulo.lados} lados.')
    print(f'El triangulo tiene {triangulo.lados} lados.')

if __name__ =='__main__':
    main()