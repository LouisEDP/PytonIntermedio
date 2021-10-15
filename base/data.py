'''
data.py
script en python que permia el regristro y consulta de libros dentro de una biblioteca.
Los libros seran modelados dentro de una clase y podran ser almacenados en 
un archivo con formato json y recuperados desde el mismo.
la bibioteca sera modelada dentro de una clase que podra administrar a los objetos 
de tipo libro.
'''
from biblioteca import Biblioteca

def main():
    bib = Biblioteca()
    bib.menu()

if __name__ == '__main__':
    main()