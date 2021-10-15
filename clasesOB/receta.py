'''REceta.py
modelo sencillo de una receta de cocina
atributos:
    ingredientes --lista de ingredientes
    pasos        --lista de pasos o instrucciones para la receta
    nombre       --nombre de la receta
coportamientos o procedimientos
    menu         --menu de operaciones
    agregar_ing  --permite agregar ingredientes
    consultar_ing--permite consultar los ingredientes
    agregar_paso --permite agregar pasos a la rectea
    consultar pasos--permite consultar los pasos de la receta'''

from ingrediente import Ingrediente
import os

class Receta:
    OPC_agregar_ing = 1
    OPC_consultar_ing = 2
    OPC_agregar_paso = 3
    OPC_consultar_paso = 4
    OPC_salir = 0

    def __init__(self, nombre=''):
        self._nombre = nombre
        self._ingredientes = []
        self._pasos = []
    
    def __str__(self):
        S = f'          {self.nombre}\n'
        S += 'Ingredientes: \n'
        for ingrediente in self.ingredientes:
            S += f'{ingrediente}\n'
        S+= '\nPasos: \n'
        for i, paso in enumerate(self._pasos):
            S+= f'{i+1}.{paso}\n'
        return S

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def ingredientes(self):
        return self._ingredientes
    @ingredientes.setter
    def ingredientes(self, valor):
        self._ingredientes = valor
    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes

    @property
    def pasos(self):
        return self._pasos
    @pasos.setter
    def pasos(self, valor):
        self._pasos = valor
    @pasos.deleter
    def pasos(self):
        del self._pasos

    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f'''            {self._nombre}
{self.OPC_agregar_ing})Agregar ingredientes.
{self.OPC_consultar_ing})Constultar ingredientes.
{self.OPC_agregar_paso})Agregar pasos.
{self.OPC_consultar_paso})Consultar pasos.

            {self.OPC_salir})Salir
            ''')
            opc = int(input('Seleciona una opcion: '))
            if opc == 1:
                self.agregar_ing()
            elif opc == 2:
                self.consultar_ing()
            elif opc == 3:
                self.agregar_pasos()
            elif opc == 4:
                self.consultar_pasos()
            elif opc == self.OPC_salir:#tecnicamtente lo mismo que haber puesto == 0 pero mas espesifico
                continuar = False
            else: 
                print('Opcion no valida')
            input('preciona enter para continuar...')
        print('nos vemos')

    def agregar_ing(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('     Agregar Ingrediente')
            nombre = input('Nombre: ')
            cantidad = -1
            while cantidad <= 0:
                cantidad = input('Cantidad: ')
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0
            unidad = input('Unidad de medida: ')
            ingrediente = Ingrediente(nombre,cantidad,unidad)
            self.ingredientes.append(ingrediente)
            respuesta = input('Deseas agregar otro ingrediente? s/n')
            if respuesta != 's' and respuesta != 'S':
                continuar = False

    def consultar_ing(self):
        os.system('cls')
        print('     Ingredientes')
        if len(self.ingredientes) == 0:
            print('No hay ingredientes registrados.')
        else:
            for ingrediente in self.ingredientes:
                print(f'{ingrediente}')

    def agregar_pasos(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('     Agregar pasos.')
            paso = input('Paso: ')
            self.pasos.append(paso)
            respuesta = input('Desea egregar mas pasos? s/n')
            if respuesta != 's' and respuesta != 'S':
                continuar = False
    def consultar_pasos(self):
        os.system('cls')
        print('     pasos.')
        if len(self.pasos) == 0:
            print('No hay pasos registrados.')
        else:
            for i, paso in enumerate(self.pasos):
                print(f'{i+1}. {paso}')