import pathlib
#buscar que tipo de archivos hay en la carpeta
def main():
    ruta = pathlib.Path('.')

    extensiones = {archivo.suffix for archivo in ruta.iterdir()}
    print(f'extensiones: {extensiones}')
if __name__ == '__main__':
    main()