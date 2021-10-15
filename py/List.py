import random
list = [1,2,3,4]
#agregar info
list.append(5)#forma de agregar un dato a la lista
list += [6,7,8]# forma de agregar mas de un dato a la lista(mas = mas+4 == mas += 1)
list.extend([9,10,7])# con el metodo extend
print(list)
#agregar en una posicion
list.insert(0,0)#(pisicion,valor nuevo)
list.insert(11,"numbers")
print(list)
print(list[5])#mostrar el dato en una posicion [-1] muestra el ultimo y menos dos el penultimo etc
#borrar 

list.pop(11)#elimina un valor(posicion) sin especificar elimina el ultimo
list.remove(0)#remueve un valor dato no la posicion
print(list)
#encontrar un valor en la lista
print(10 in list)
print(list.index(8))
print(list.index(7, 8))#(valor a buscar, apartir de donde buscar)
print(list.count(7))
# copiar lista l2 = l1[:]
print(list[1:8]) # muestra el congenido de una lista [inicio:fin  : de dos en dos uno en uno etc]
ran = [random.randint(1,100) for i in range(7)]
print(ran)
matriz = [['a','b','c'], ['d','e','f'], ['g','h','i']]
print(matriz[2][1])#[num fila][num columna]