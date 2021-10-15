#d = {1:'uno', 2:'dos', 3:'tres'}
d = dict([ (1, 'uno'), (2, 'dos'), (3, 'tres') ])
d[4] = 'cuatro' #[llave] = valor...tambien sirve para cambiar valores
d.setdefault(5, 'cinco')
print(d)
print(d.get(4, 'que')) # si no existe la llave mostraria el mansaje 'que'
