'''
Script en Python que utilice el menu de una clase Receta dentro de la cual 
habra una lista de ingredientes. Cada Ingrediente tendra como atributo los 
siguientes:
    -nombre
    -cantidad
    -inidad de medida
la clase Receta ademas de contener un menú y una lista de ingredientes deberá
tener un nombre y una lista de pasos o nstrucciones as como los siguientes 
comportamientos:
    -agregar ingredientes
    -consultar ingredientes
    -agregar pasos
    -consultar pasos
    '''
from receta import Receta

def main():
    receta = Receta('dos molletes')

    receta.menu()
    print(receta)

if __name__=='__main__':
    main()