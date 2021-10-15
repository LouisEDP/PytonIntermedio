import os

Agregar = 1
Mostrar = 2
Buscar = 3
Modificar = 4
Eliminar = 5
Salir = 0

def Mostrar_menu():
    os.system('cls')
    print(f'''         Agenda
    {Agregar}) Agregar contacto
    {Mostrar}) Mostrar contacto
    {Buscar}) Buscar contacto
    {Modificar}) Modificar contacto
    {Eliminar}) Eliminar contacto
    {Salir}) Salir''')

def Agregar_contactos(agenda):
    os.system('cls')
    print('      Agregar contacto')
    Nombre = input('ingrese el nombre: ')
    if Nombre in agenda:
        print('Ya exites este contacto...')
    else:
        Telefono = input('ingrese telefono: ')
        Email = input('ingrese email: ')
        agenda[Nombre] = (Telefono, Email)
        print('contacto agregado con exito...')

def Mostrar_contactos(agenda):
    os.system('cls')
    print('      Lista de contactos:')
    if len(agenda) > 0:
        for k, v in agenda.items():
            print(f'Nombre: {k}')
            print(f'Telefono: {v[0]}')
            print(f'Email: {v[1]}')  
            print('#'*20)
    else:
        print('No hay contactos aun...')

def Buscar_contacto(agenda):
    os.system('cls')
    print('     Buscar contactos')
    if len(agenda) > 0:
        Nombre = input('Nombre: ')
        Coincidencias = 0
        for k, v in agenda.items():
            if Nombre in k:
                print(f'Nombre: {k}')
                print(f'Telefono: {v[0]}')
                print(f'Email: {v[1]}')  
                print('#'*20)
                Coincidencias += 1
        if Coincidencias == 0:
            print('no se encontro el contacto')
    else:
        print('Aun no hay contactos como para buscar')

def Modificar_contactos(agenda):
    os.system('cls')
    print('         modificar contacto')
    if len(agenda) > 0:
        Nombre = input('Nombre: ') 
        if agenda.get(Nombre):
            v = agenda.get(Nombre)
            print(f'Nombre: {Nombre}')
            print(f'Telefono: {v[0]}')
            print(f'Email: {v[1]}')  
            print('#'*20)
            print('ingrese los nuevos datos: ')
            Telefono = input('Telefono: ')
            Email = input('Email: ')
            agenda[Nombre] = (Telefono, Email)
            print('Datos actualizados...')
        else:
            print('No existe el contacto')
    else:
        print('No hay contactos...')

def Eliminat_contacto(agenda):
    os.system('cls')
    print('           Eliminar contacto')
    if len(agenda) > 0:
        Nombre = input('Nombre: ')
        if Nombre in agenda:
            agenda.pop(Nombre)
            print('Contato eiliminado...')
        else:
            print('No se encontro el contacto')
    else:
        print('No hay contactos para borrar')

def main():
    continuar = True
    Mi_agenda = {}
    while continuar:
        Mostrar_menu()
        seleccion = int(input('seleccione una opcion: '))
        if seleccion == Agregar:
            Agregar_contactos(Mi_agenda)
        elif seleccion == Mostrar:
            Mostrar_contactos(Mi_agenda)
        elif seleccion == Buscar:
            Buscar_contacto(Mi_agenda)
        elif seleccion == Modificar:
            Modificar_contactos(Mi_agenda)
        elif seleccion == Eliminar:
            Eliminat_contacto(Mi_agenda)
        elif seleccion == Salir:
            continuar = False
        else:
            print('Opcion invalida.')
        input('Precione enter para continuar...')

if __name__=='__main__':
    main()