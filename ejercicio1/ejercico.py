'''
Ejercicio de Herencia
Script en Pthon que solicite la informacion de un objeto de tipo 
Estudiante y posteriormente imprima en pantalla sus datos. 
La clase Estudiante heredara de la clase Persona, es decr que sera un 
tipo particular de persona. Un Estudiante ademas de la informacion y 
comportamientos de una persona tendrá como atributos un promedio y un codigo 
de estudiante y como comportamiento podra estudiar una materia. Finalmente
hacer que el estuiante ejecuta el comportamiento "estudiar".
'''
from persona import Persona
from estudiante import Estudiante

def main():
    nombre = input('Nombre: ')
    edad = input('edad: ')
    codigo = input('Id codigo: ')
    promedio = int(input('prmedio: '))

    estudiante = Estudiante(nombre, edad, codigo, promedio)
    print(f'''Datos de estudiante:
{estudiante}''')

    estudiante.estudiar('Programacino Orientada a Objetos')

if __name__=='__main__':
    main()