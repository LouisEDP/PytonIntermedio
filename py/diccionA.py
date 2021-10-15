import pathlib

def main():
    ruta = pathlib.Path('.')
#diccionario con compatacion y sub compactacion de lista
    diccionario = {k : [v.name for v in ruta.glob(f'*{k}')]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}
    
    for extension, archivos in diccionario.items():
        print(f'extension: {extension}')
        print(f'archivos: {archivos}')

if __name__ == '__main__':
    main()