lista = [111, 'squanch', 1.3]
# agregar elementos a lista
print('Lista >>> ', lista)
lista.append('storm')
print('lista @ lista* 3 >>> ', lista * 3)
print('agregar elementos a lista @lista.append(value) >>> ', lista, '\n')
# si no se le coloca un parametro a pop(),
# retorna el ultimo elemento de la lista y lo elimina
lista.pop(2)
print('Eliminar elementos de la lista @lista.pop(2)  >>> ', lista)
del lista[0]
print('eliminar @del lista[0] >>> ', lista)
#
#ordenar asc y des con sort() y reverse()
abecedario = ['a', 'b', 'c', 'd', 'f', 'e', 'g']
print('lista >>> ', abecedario)
abecedario.sort()
print('ordenado @lista.sort() >>> ', abecedario)
abecedario.reverse()
print('ordenado @lista.reverse() >>> ', abecedario)
print('\nITERANDO LISTA >>> ')
for c in [1, 2, 3, 5, 6, 7]:
    print(c)
print('meotodos')
lista.extend([2, 5])
print('añador elementos al final de la lista @ lista.extend([2, 5]) >>> ', lista)



