def validar_cadena(cadena):
    pila = []
    for simbolo in cadena:
        if simbolo == '(':
            pila.append('(')
        elif simbolo == ')':
            if len(cadena) > 0:
                pila.pop()
            else:
                return False
    return len(pila) == 0

def main():
    print('ingrese una horacion entre parentesis')
    o = input('oracion: ')
    validar = validar_cadena(o)

    if validar:
        print('La oracion esta escrita con un numero igual de parentesis y se encuentran en orden')
    else:
        print('La esprecion no tiene la misma cantidad de parentesis o estos estan en desorden')

if __name__ == '__main__':
    main()