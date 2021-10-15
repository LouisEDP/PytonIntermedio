'''
script en Python que cree e imporima la informacion de un objeto de tipo
persona y de otro de tipo deportista.
las clases deportista heredara de la clase persona, es decir que sera
un tipo de particular de persona.
'''
from persona import Humano
from deportista import Deportista
def main():
    per_1 = Humano('Hector Tuga', 44)
    deportista = Deportista('Pepe Nava', 33, 'natacion')

    print(f'''Datos de la persona:
{per_1}''')
    print('*'*40)
    print(f'''Datos deportista:
{deportista}''')

    deportista.entrenar()
    deportista.hablar('listo para el 3° lugar')
if __name__=='__main__':
    main()