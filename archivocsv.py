import os, csv

def aregar_pelicula(nombre_archivo):
    cantidad = int(input('¿Cuantas peliculas se registrara?: '))
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter = ',')
        for i in range(cantidad):
            os.system('cls')
            titulo = input('Titulo: ')
            duracion = input('Duracion: ')
            anio = input('Año: ')
            writer.writerow([titulo, duracion, anio])

def ver_pelicular(nombre_archivo):
    os.system('cls')
    print('Pelicular Registradas: ')
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for linea in reader:
            print(f'Titulo: {linea[0]}')
            print(f'Duracion: {linea[1]}')
            print(f'Año: {linea[2]}')
def main():
    archivo = 'peliculas.csv'
    aregar_pelicula(archivo)
    ver_pelicular(archivo)

if __name__=='__main__':
    main()
