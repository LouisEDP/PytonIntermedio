import random, os

Intentos_maximos = 6
Paises = ['Mexico', 'Argentina', 'Brasil', 'Chile', 'Bolivia', 'Ecuador', 'Peru', 'Canada', 'Uriguay', 'Costa Rica']

def Seleccionar_pais():
    Pais = random.choice(Paises)
    Secreto = '_'*len(Pais)
    return Pais, Secreto

def Reemplazar_simbolo(Original,Secreto,Simbolo):
    Cantidad = Original.count(Simbolo)
    inicio = 0
    for i in range(Cantidad):
        pos = Original.find(Simbolo, inicio)
        Secreto = Secreto[:pos] + Simbolo + Secreto[pos+1:]
        inicio = pos + 1
    return Secreto

def Ahorcado():
    print(f'Bienvenido al juego del ahorcado, la palabra secreta \
sera el nombre de un Pais de America, Tienes {Intentos_maximos} intentos')
    input('Presiona Enter para comenzar >')
    os.system('cls')
    Original , Secreto = Seleccionar_pais()
    Fallos = 0
    while Secreto != Original and Fallos < Intentos_maximos:
        os.system('cls')
        print(f'El Pais es: {Secreto}')
        S = input('Adivina una letra: ')
        if S in Original:
            Secreto = Reemplazar_simbolo(Original,Secreto,S)
            print('Bien')
        else:
            print('nel')
            Fallos += 1
            print(f'llevas {Fallos} oportunidades de {Intentos_maximos}')
        input('Presiona Enter parar continuar...')
    os.system('cls')
    if Secreto == Original:
        print(f'Felicidades el Pais es: {Original}>>>{Secreto}')
    else:
        print(f'mala suerte, el pais era: {Original}')
    print('nos vemos.')

def main():
    Ahorcado()
if __name__=='__main__':
    main()

'''
seleccionar un pais
Original , Secreto = Seleccionar_pais()
print(Original)
print(Secreto)

Secreto = Reemplazar_simbolo('Mexa','____','x')
print(Secreto)
'''