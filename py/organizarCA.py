import pathlib

def main():
    ruta = pathlib.Path('.')
    diccionario = {k : [v for v in ruta.glob(f'*{k}')]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}
    
    for extension, archivos in diccionario.items():
        carpeta = ruta / extension[1:]
        carpeta.mkdir()
        for archivo in archivos:
            archivo.replace(carpeta / archivo.name)

if __name__=='__main__':
    main()