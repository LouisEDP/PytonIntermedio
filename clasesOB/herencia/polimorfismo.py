'''
Script en Python que simule un personaje y un grupo de enemigos que podran,
atacar al personaje principal de forma especial segun su naturaleza.
los enemigos seran modelados con calses y se hara uso de polimosfrimo para
permitirles atacar de manera porsonalizada.
    Bloque para mostrar los enemigos -->
    for e in enemigos:
            os.system('cls')
            e.atacar()
            input('preciona enter para continuar...')

'''
import enemigo
import os
import random
def main():
    enemigos = []
    for i in range(5):
        tipo_enemigo = random.randint(0, len(enemigo.tipos)-1)
        if tipo_enemigo == enemigo.MOMIA:
            enemigos.append(enemigo.Momia())
        elif tipo_enemigo == enemigo.ZOMBI:
            enemigos.append(enemigo.Zombi())
        else:
            enemigos.append(enemigo.Vampiro())

    personaje = {'energia':100, 'fuerza':6} #diccionario para atributos
    GANANCIA_ENERGIA = 5
    INCREMENTO_FUERZA = 4

    while personaje['energia'] > 0 and len(enemigos) > 0:
        while personaje['energia'] > 0 and enemigos[0].energia > 0:
            os.system('cls')
            print(f'Energia del Pedorro: {personaje["energia"]}       Energia de {enemigos[0].tipo}: {enemigos[0].energia}')
            enemigos[0].atacar()
            personaje['energia'] -= enemigos[0].fuerza
            if personaje['energia'] > 0:
                print(f'Has atacado a {enemigos[0].tipo} y cuaso {personaje["fuerza"]} de daño')
                enemigos[0].energia -= personaje['fuerza']
                input('continuar batalla...')
        if personaje['energia'] > 0:
            os.system('cls')
            print(f'Energia del Pedorro: {personaje["energia"]}       Energia de {enemigos[0].tipo}: {enemigos[0].energia}')
            print(f'Has derrotado a {enemigos[0].tipo}')
            print(f'Has recuperado: {GANANCIA_ENERGIA} de energia')
            print(f'Tu fuerza aumento: {INCREMENTO_FUERZA} puntos')
            personaje['energia'] += GANANCIA_ENERGIA
            personaje['fuerza'] += INCREMENTO_FUERZA
            enemigos.pop(0)
            input('continuar aventura...')
    if personaje['energia'] > 0:
        print('Has vencido a todos los enemigos...')
    else:
        print('GAME OVER X.X')

                    

if __name__ == '__main__':
    main()