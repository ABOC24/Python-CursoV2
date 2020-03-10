# Tipo de dato compuesto: diccionario

# 1. Creación de diccionarios:
diccionario_1 = {'propiedad1': 1, 'propiedad2': 2, 'propiedad3': [1, 2, 3]}
diccionario_2 = dict()
diccionario_2['propiedad1'] = 1
diccionario_2['propiedad2'] = 2
diccionario_2['propiedad3'] = [1, 2, 3]

print(diccionario_1)
print(type(diccionario_1))
print()
print(diccionario_2)
print(type(diccionario_2))

print()

computador = {'id': 1001, 'marca': 'MSi', 'ram': 128, 'cpu': 'Intel Core i7 Extreme Edition', 'almacenamiento': 8}
print(computador)
print(f'La variable diccionario `computador` tiene {len(computador)} propiedades.')
print('El tipo de dato de la variable `computador` es: %s' % type(computador).__name__)

print()

# 2. Acceso a las propiedades y valores de un diccionario:
print('Acceso a las propiedades y valores de un diccionario:')
print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['ram']}")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")
print('Cantidad de propiedades del diccionario `computador`:', len(computador))

print()

print(computador.get('Almacenamiento', '1'))
print(computador.get('tarjeta_grafica', 'integrada'))

print()

# 3. Modificación del contenido de un diccionario:
computador['marca'] = 'Alienware'
computador['id'] = 2001
computador['gpu'] = 'NVIDIA GeForce RTX 2080 8GB'

print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['ram']}")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")
print(f"GPU: {computador['gpu']}")
print('Cantidad de propiedades del diccionario `computador`:', len(computador))

print()

# 3. Iteración de un diccionario:
print('3. Iteración de un diccionario:')
# 3.1 Iteración por las llaves de un diccionario:
print('3.1 Iteración por las llaves de un diccionario:')

for k in computador.keys():
    print(f'{k.upper()}: {computador[k]}')

print()

# 3.2 Iteración por los valores de un diccionario:
print('3.2 Iteración por los valores de un diccionario:')

for v in computador.values():
    print(v)

print()

# 3.3 Iteración por las llaves y los valores de un diccionario:
print('3.3 Iteración por las llaves y los valores de un diccionario:')

for k, v in computador.items():
    print(f'{k.upper()}: {v}')

print()

# 3.4 Métodos y operadores para variables de tipo diccionario:
# 3.4.1 list(): para convertir las llaves de un diccionario en una lista:
print('3.4.1 list(): para convertir las llaves de un diccionario en una lista:')
atributos = list(computador)
print(atributos)
print('Cantidad de llaves (atributos) del diccionario `computador`:', len(atributos))

print()

# 3.4.2 in: para consultar si una llave se encuentra en un diccionario:
print('3.4.2 in: para consultar si una llave se encuentra en un diccionario:')
print('board' in computador)
print('gpu' in computador)
