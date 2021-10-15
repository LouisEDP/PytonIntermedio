import os

Agregar = 1
Insertar = 2
Mostrar = 3
Buscar = 4
Eliminar = 5
Ordenar = 6
Limpiar = 7
Salir = 0
Frutas = []

def Imprimir_menu():
    os.system('cls')
    print(f'''              Frutas
        {Agregar}) Agregar
        {Insertar}) Insertar
        {Mostrar}) Mostrar
        {Buscar}) Buscar
        {Eliminar}) Eliminar
        {Ordenar}) Ordenar
        {Limpiar}) Limpiar Lista
        {Salir}) Salir''')

def Agregar_nueva():
    print('            Agregar')
    nueva = input('Nombre: ')
    Frutas.append(nueva)
    print('Agregada')


def Ingresar_nueva():
    print('            Insertar')
    nueva = input('Nombre: ')
    posicion = int(input('Posicion: '))
    Frutas.insert(posicion, nueva)
    print(f'Registro ingresado en la posicion {posicion}')

def Mostrar_lista():
    print('            Mostrar')
    if len(Frutas) > 0:
        for Nombre in Frutas:
            print(Nombre)
    else:
        print('No se a agregado nada')

def Buscar_registro():
    print('          Buscar')
    if len(Frutas) > 0:
        Nombre = input('Nombre a buscar: ')
        if Nombre in Frutas:
            cantidad = Frutas.count(Nombre)
            inicio = 0
            for i in range(cantidad):
                pos = Frutas.index(Nombre, inicio)
                print(f'{Nombre} se encuantra en la posicion {pos+1}')
                inicio = pos + 1
        else:
            print(f'No se encuantra {Nombre} en la lista')
    else:
        print('No hay regstros')

def Eliminar_registro():
    print('             Eliminar')
    if len(Frutas) > 0:
        for i in range(len(Frutas)):
            print(f'{i+1}. {Frutas[i]}')
        print('0. Cancelar')
        pos =  int(input(f'Posicion a eliminar desde 1 a {len(Frutas)}:'))
        if 0 < pos <= len(Frutas):
            Frutas.pop(pos-1)
            print('El registro se elimino')
        else:
            print('No se elimino ningun registro')
    else:
        print('No hay nada en la lista por borrar')

def Ordenar_registros():
    print('               Ordenar')
    if len(Frutas)  > 0:
        Frutas.sort()
        print('Se ordeno alfabeticamente')
    else:
        print('No se hay nada en la lista para poder ordenar')
        
def Limpiar_registros():
    print('             Limpiar')
    Frutas.clear()
    print('Se a borrado todo en la lista')

def main():
    Continuar = True
    while Continuar:
        Imprimir_menu()
        Opcion = int(input('Selecciona una opcion: '))
        os.system('cls')
        if Opcion == Agregar:
            Agregar_nueva()
        elif Opcion == Insertar:
            Ingresar_nueva()
        elif Opcion == Mostrar:
            Mostrar_lista()
        elif Opcion == Buscar:
            Buscar_registro()
        elif Opcion == Eliminar:
            Eliminar_registro()
        elif Opcion == Ordenar:
            Ordenar_registros()
        elif Opcion == Limpiar:
            Limpiar_registros()
        elif Opcion == Salir:
            print('Nos vemos prro')
            Continuar = False
        else:
             print('Opcion no valida')
        input('precione enter para continuar')
if __name__ == '__main__':
    main()