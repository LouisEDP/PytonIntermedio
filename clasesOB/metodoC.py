
from claseM import Prenda

def main():
    camisa = Prenda()

    camisa.tipo = 'Playera cuello V'
    camisa.talla = 'M'

    pantalon = Prenda()

    pantalon.tipo = 'Mezclilla'
    pantalon.talla = '32'

    print(camisa)
    print(pantalon)

if __name__=='__main__':
    main()
