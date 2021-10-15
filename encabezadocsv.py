import os, csv, pathlib

def agregar_dato(nombre_archivo):
    cantidad = int(input('cantiad de pelicular a registrar?: '))
    header = ['Titulo', 'Duracion', 'Año']

    if not pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames = header)
            writer.writeheader()
    
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames = header)
        for i in range(cantidad):
            os.system('cls')
            titulo = input('Titulo: ')
            duracion = input('Duracion: ')
            anio = input('Año: ')
            writer.writerow({'Titulo': titulo,
                            'Duracion': duracion,
                            'Año': anio
            })
def ver_pelicular(nombre_archivo):
    os.system('cls')
    print('Pelcular Registradas: ')
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for linea in reader:
            for k,v in linea.items():
                print(f'{k}: {v}')
            print('/'*30)

def main():
    archivo = 'Pelicular_encabezado.csv'
    agregar_dato(archivo)
    ver_pelicular(archivo)

if __name__=='__main__':
    main()