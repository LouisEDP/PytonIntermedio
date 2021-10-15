import os, pathlib

Salir = 0
Agregar = 1
Mostrar = 2
Buscar = 3

def mostrar_menu():
    os.system('cls')
    print(f'''         Agenda reutilizable
    {Agregar}) Agregar contacto.
    {Mostrar}) Mostrar contacto.
    {Buscar}) Buscar contacto.

    {Salir}) salir.
    ''')
def cargar_agenda(txt,nombre_txt):
    if pathlib.Path(nombre_txt).exists():
        with open(nombre_txt, 'r') as archivo:
            for renglon in archivo:
                contacto, telefono, email = renglon.strip().split(', ')
                txt.setdefault(contacto, (telefono, email))
    else:
        with open(nombre_txt, 'w') as archivo:
            pass

def Agregar_contacto(txt, nombre_txt):
    os.system('cls')
    print('    Agregar contacto.')
    nombre = input('Nombre: ')
    if txt.get(nombre):
        print('Ese nombre ya existe')
    else:
        telefono = input('Telefon: ')
        email = input('Email: ')
        txt.setdefault(nombre, (telefono, email))
        with open(nombre_txt, 'a') as archivo:
            archivo.write(f'{nombre}, {telefono}, {email}\n')
        print('Contacto Agregado...')

def Mostrar_contacto(txt):
    os.system('cls')
    print('       Contactos')
    if len(txt) > 0:
        for k, v in txt.items():
            print(f'Nombre: {k}')
            print(f'Telefono: {v[0]}')
            print(f'Email: {v[1]}')
            print('/'*40)
    else:
        print('No hay cotactos registrados...')

def Buscar_contacto(txt):
    os.system('cls')
    print('     Buscar contactos.')
    if len(txt) > 0:
        nombre = input('Ingrese el nombre del contacro a buscar: ')
        found = 0
        for k, v in txt.items():
            if nombre in k:
                print(f'Nombre: {k}')
                print(f'Telefono: {v[0]}')
                print(f'Email: {v[1]}')
                found += 1
        if found == 0:
            print('No se encontro councidencias...')
        else:
            print(f'se econtraron {found} contactos...')
    else:
        print('No hay cotactos registrados...')

def main():
    continuar = True
    txt = dict()
    nombre_txt = 'agenda.txt'
    cargar_agenda(txt, nombre_txt)

    while continuar:
        mostrar_menu()
        opc = int(input('selecciona una opcion: '))

        if opc == 1:
            Agregar_contacto(txt, nombre_txt)
        elif opc == 2:
            Mostrar_contacto(txt)
        elif opc == 3:
            Buscar_contacto(txt)
        elif opc == 0:
            continuar = False
        else: 
            print('opcion no valida')
        input('precione enter para continuar...')
    print('Eso es todo')

if __name__ == '__main__':
    main()