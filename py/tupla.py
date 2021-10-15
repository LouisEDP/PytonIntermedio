import os

Agregar = 1
Consultar = 2
Salir = 0

def mostrar_menu():
    os.system('cls')
    print(f'''        Catalogo de mascotas
    {Agregar}) Añadir mascota.
    {Consultar}) Cosultar mascota.
    {Salir}) Salir''')

def Agregar_mascota(mascotas):
    os.system('cls')
    print('Regsitrar mascota: ')
    nombre = input('Nombre: ')
    edad = int(input('Edad: '))
    peso = float(input('Peso: '))
    tipo = input('Tipo: ')
    mascotas.append( (nombre, edad, peso, tipo) )

def Consulta_mascotas(mascotas):
    os.system('cls')
    print('Lista de mascotas: ')

    if len(mascotas) == 0:
        print('No hay registros...')
    else:
        for mascota in mascotas:
            nombre, edad, peso, tipo = mascota
            print(f'Nombre: {nombre}')
            print(f'Edad: {edad}')
            print(f'Peso: {peso}')
            print(f'Tipo: {tipo}')
            print(f':v :v :v :v :v :v :v'*2)
def main():
    mis_mascotas = []
    continuar = True
    while continuar:
        mostrar_menu()
        seleccion_opcion = int(input('selecciona una opcion: '))
        if seleccion_opcion == Agregar:
            Agregar_mascota(mis_mascotas)
        elif seleccion_opcion == Consultar:
            Consulta_mascotas(mis_mascotas)
        elif seleccion_opcion == Salir:
            continuar = False
        else:
            print('Opcion no valida...')
        input('preciona enter para continuar...')
    input('Eso es todo... :v/')

if __name__ == '__main__':
    main()