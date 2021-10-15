'''
POO_8.py
script en Python que tenga una lista de objetos tipo Pelicula. la lista debera
ser ordenada segun el numero de las peliculas, una vez ordenada se mostrará
la lista ademas del menos y mayor objeto de la colección.
'''

from pelicula import Pelicula


def main():
    peliculas = []
    peliculas.append(Pelicula('lo que sea', 'El Chido', 1999, 45))
    peliculas.append(Pelicula('lo que sea', 'El Chido', 1999, 45))
    peliculas.append(Pelicula('lo que sea parte 2', 'El Chido', 2001, 120))
    peliculas.append(Pelicula('el chupas', 'martyn', 2019, 135))
    peliculas.append(Pelicula('la mara', 'El Chido', 2015, 148))
    peliculas.append(Pelicula('lo que sea parte 3', 'El Chido', 2021, 230))

    peliculas.sort()

    print(peliculas[3] <= peliculas[4])

    print(peliculas[2] == peliculas[3])


    for p in peliculas:
        print(p)
        print('/'*50)

    print(f'menor pelicula en la coleccion: {max(peliculas)}')


if __name__== '__main__':
    main()