#los Dictionaries estan compuestos por una <clave, valor>
diccionario = {'name': 'kevin', 'age': 23}
print('Diccionario >>> ', diccionario)
#obteniendo valor por la llave
print('@ diccionario["name"] >>> ', diccionario['name'])
#
#modificar elementos al diccionario
diccionario['name'] += ' Figueroa'
print('Modificando -> @diccionario["name"] += " Figueroa" >>> ', diccionario)
keyvalue = {'a': 1, 'c': 3, 'b': 2}
print('diectorio >>> ', keyvalue)
print(keyvalue.values())
keyDirectory = list(keyvalue.keys())
print('keys >>', (keyDirectory))
keyDirectory.sort()
print('sort >>> ', (keyDirectory))
# crear un diccionario vacio y llenarlo por asignación
dic = {}
print('diccionario vacio @dic ={} >>> ', dic)
dic['key'] = 'valor'
dic['key2'] = 'valor2'
dic['key3'] = 'valor3'
print('asignar <clave valor > @dic["key"] = "valor" >>> ', dic, '\n')


##
# operaciones con Dictionaries mas complejos
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






