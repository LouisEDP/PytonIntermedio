string = 'Cadena de feria'

print(string)
print(string[2])
print(string[2:5])
print(string.count('a'))#contar el caracter 
print(string.find('a'))#encontrar el primer caracter
print(string.find('a',2))
print('d' in string)

print('+'.join(string))
print('+'.join(['1','2','3'])) #parece que no funciona con int solo char

print(string.replace('a','A'))
print(string.replace('a','A',1))#valor a vambiar, cambio, veces que se cambiara
#cambiar una cadena por pedazos
string = string[:2] + 'nti' + string[4:]
print(string)

print(string.split(' '))