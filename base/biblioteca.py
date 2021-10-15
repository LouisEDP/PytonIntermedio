'''
biblioteca.py
Modelo sencillo de una biblioteca.
Atributos:
    libros                --coleccion de libros de la biblioteca.
Metodos:
    recuperar_libro(ruta) --recupera los ibros desde el arcivo indicado por ruta.
    almacenar_libro(ruta) --almacena los libros en el archivo indicado por ruta.
    agregar_libro(ruta)   --agrega un libro en la coleccion de la biblioteca.
    consultar_libros      --consultar los libros de la biblioteca.
    menu                  --menu para la biblioteca.
'''

import json
from libro import *
import os
import pathlib


class Biblioteca:
    Agregar_Libro = 1
    Consultar_Libros = 2
    Salir = 0

    def __init__(self):
        self._libros = []
        self.recuperar_libros('libros.json')

    #Destructor de calse
    def __del__(self):
        self.almacenar_libros('libros.json')

    @property
    def libros(self):
        return self._libros
    @libros.setter
    def libros(self, valor):
        self._libros = valor
    @libros.deleter
    def libros(self):
        del self._libros

    def recuperar_libros(self, ruta):
        if pathlib.Path(ruta).exists():
            with open(ruta, 'r') as archivo:
                datos = json.load(archivo)
            for lib in datos['libros']:
                self.libros.append(desde_json(lib))

    def almacenar_libros(self, ruta):
        with open(ruta, 'w') as archivo:
            json.dump({'libros':self.libros}, archivo, cls=Libro_Encoder, indent=4)

    def agregar_libros(self):
        os.system('cls')
        print('         Agregar libros:')
        isbn = input('isbn: ')
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        self.libros.append(Libro(isbn, titulo, autor))

    def consultar_libros(self):
        os.system('cls')
        print('         Consultar libros')
        if len(self.libros) == 0:
            print('No hay libros regsitrados')
        else:
            for lib in self.libros:
                print(f'{lib}')
                print('+'*55)

    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f'''          Biblioteca Mamalona
{Biblioteca.Agregar_Libro}) Agregar libro.
{Biblioteca.Consultar_Libros}) Consultar libros.
{Biblioteca.Salir}) Salir.''')
            opc = input('selecciona una opcion: ')
            try:
                opc = int(opc)
            except:
                opc = -1
            if opc == Biblioteca.Agregar_Libro:
                self.agregar_libros()
            elif opc == Biblioteca.Consultar_Libros:
                self.consultar_libros()
            elif opc == Biblioteca.Salir:
                continuar = False
            else:
                os.system('cls')
                print('opcion no valida.')
            input('Precione enter para continuar...')
        input('Preciona enter para salir.')