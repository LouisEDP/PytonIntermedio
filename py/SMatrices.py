import random, os

X = int(input('Ingrese el tamaño de las matrices a sumar: '))

print(f'Este programa suma matrices de tamaño {X} * {X}')

M1 = [[random.randint(1,50) for i in range(X)] for j in range(X)]

M2 = [[random.randint(1,50) for i in range(X)] for j in range(X)]
'''
Suma = [[0]*X for i in range(X)]

for renglon in range(X):
    for columna in range(X):
        Suma[renglon][columna] = M1[renglon][columna] + M2[renglon][columna]
'''
Suma = [[M1[i][j]+M2[i][j] for j in range(X)] for i in range(X)]

'''
for i in range(X):
    if i == X//2:
        print(f'{M1[i]} + {M2[i]} = {Suma[i]}')  
    else: 
        print(f'{M1[i]}  {M2[i]}  {Suma[i]}')
'''
for i in range(X):
    print(f'{M1[i]} + {M2[i]} = {Suma[i]}') if i == X//2 else print(f'{M1[i]}  {M2[i]}  {Suma[i]}')
