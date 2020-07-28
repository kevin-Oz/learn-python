#los diccionarios estan compuestos por una <clave, valor>
diccionario = {'name': 'kevin', 'age': 23}
print(diccionario)
#obteniendo valor por la llave
print(diccionario['name'])
#
#modificar elementos al diccionario
diccionario['name'] += ' Figueroa'
print(diccionario)
# crear un diccionario vacio y llenarlo por asignación
dic = {}
print(dic)
dic['key'] = 'valor'
dic['key2'] = 'valor2'
dic['key3'] = 'valor3'
print(dic, '\n')
##
# operaciones con diccionarios mas complejos
worker = {
    'name': {'first': 'kevin', 'last': 'figueroa'},
    'job': ['dev', 'mgr'],
    'age': 23
}
#
#obtener info especifica
print(worker['name'])
print(worker['name']['last'], worker['job'][0])
worker['job'].append('janitor')
print(worker)
worker = 0
print(worker)
##
#






