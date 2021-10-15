import os, pathlib

Salir = 0
Agregar = 1
Mostrar = 2

def mostrar_menu():
    os.system('cls')
    print(f'''         Agenda reutilizable
    {Agregar}) Agregar contacto.
    {Mostrar}) Mostrar contacto.

    {Salir}) salir.
    ''')

def cargar_stories(txt,nombre_txt):
    if pathlib.Path(nombre_txt).exists():
        with open(nombre_txt, 'r') as archivo:
            for renglon in archivo:
                descripcion, nombre, tiempo = renglon.strip().split(', ')
                txt.setdefault(descripcion, (nombre, tiempo))
    else:
        with open(nombre_txt, 'w') as archivo:
            pass

def Agregar_stream(txt, nombre_txt):
    os.system('cls')
    print('    Agregar stream.')
    descripcion = input('descripcion: ')
 #   if txt.get(nombre):
  #      print('Ese nombre ya existe')
   # else:
    nombre = input('Nombre del stream: ')
    tiempo = input('tiempo: ')
    txt.setdefault(descripcion, (nombre, tiempo))
    with open(nombre_txt, 'a') as archivo:
        archivo.write(f'{descripcion}, {nombre}, {tiempo}\n')
    print('Contacto Agregado...')

def Mostrar_guardados(txt):
    os.system('cls')
    print('       Hagen Stories')
    if len(txt) > 0:
        for k, v in txt.items():
            print(f'Descipcion: {k}')
            print(f'Nombre del Stream: {v[0]}')
            print(f'tiempo: {v[1]}')
            print('/'*40)
    else:
        print('No hay streams registrados...')

def main():
    continuar = True
    txt = dict()
    nombre_txt = 'hagen.txt'
    cargar_stories(txt, nombre_txt)

    while continuar:
        mostrar_menu()
        opc = int(input('selecciona una opcion: '))

        if opc == 1:
            Agregar_stream(txt, nombre_txt)
        elif opc == 2:
            Mostrar_guardados(txt)
        elif opc == 0:
            continuar = False
        else: 
            print('opcion no valida')
        input('precione enter para continuar...')
    print('Eso es todo')

if __name__ == '__main__':
    main()