import os, queue

Agendar = 1
Atender = 2
Salir = 0

def pantalla_menu():
    os.system('cls')
    print(f'''         Agenda     
    {Agendar} Agregar evento
    {Atender} Atender evento
    {Salir} Salir''')

def Agendar_evento(evento):
    print('     Ingrese el evento ')
    ag = input('Evento: ')
    evento.put(ag)

def Atender_evento(evento):
    print('     Atender evento')
    if evento.empty():
        print('No hay eventos por atender.')
    else:
        ag = evento.get()
        print(f'Evento: {ag}')

def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        pantalla_menu()
        seleccion = int(input('seleccione una opcion: '))
        os.system('cls')
        if seleccion == 1:
            Agendar_evento(agenda)
        elif seleccion == 2:
            Atender_evento(agenda)
        elif  seleccion == 0:
            continuar = False
        else:
            print('selecciono una opcion no valida...')
        input('precione enter para continuar...')

if __name__=='__main__':
    main()