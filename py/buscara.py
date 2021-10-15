import pathlib

ruta = pathlib.Path('.')
'''
for archivo in ruta.glob('*.py'):# iterdir para todo en lugar de glob
    print(archivo)'''

print('programa que busca un archivo dentro de la carpeta de trabajo')
archivo = input('ingrese el nombre del archivo a buscar: ')
archivo = ruta / archivo

if archivo.exists():
    print(f'el archivo existe y mide {archivo.stat().st_size} bytes')
else:
    print('el archivo no existe')