# matriz de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('matriz >> ', matriz)
print('obtener fila >> ', matriz[1])
print('obtener elemento >> ', matriz[1][1])
##
# Obteniendo todos los elementos en la posicion 1 de cada fila de la matriz
elements = [row[1] for row in matriz]
print('elementos posicion[1] >> ', elements)
# Obteniendo los elementos en la posicion 1 de cada fila de la matriz y que sea numero par
elements = [row[1] for row in matriz if row[1] % 2 == 0]
print('elementos posicion[1] mod2 >> ', elements)
#
##iteracion de la matriz en posiciones 0,1,2 de la matriz
diagonal = [matriz[i][i] for i in [0, 1, 2]]
print('Elementos en Diagonal matriz >>> ', diagonal)
#
## repitiendo caracteres de un string
duplicate = [c * 2 for c in 'parangutirimicuaro']
print(duplicate)
#
# generando sumador de elementos de la fila
sumador = [sum(row) for row in matriz]
print('\nsumando elementos de cada fila', sumador)
# next(sumador) --> iterar elementos
print('diccionario >>> ', {sum(row) for row in matriz})
# imprime la suma de las posiciones de la matriz, itera hasta la posicion 3 (range)
print('\n diccionario  <clave valor>  >>', {i: sum(matriz[i]) for i in range(3)})
#


