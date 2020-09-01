name = 'wasovsky'
age = '32'
frutas = 'banana,uva,fresa,mango'
print('lista de frutas @frutas.split(",") >>> ', frutas.split(','), '\n')
#
print('UPPER - LOWER')
print('@frutas.upper() >>> ', frutas.upper())
print('@frutas.lower() >>> ', frutas.lower(), '\n')
#
print('verificar si es texto o numero el string \n @ name.isalpha(), age.isdigit() >>> ', name.isalpha(), age.isdigit())
#
line = 'hola mundo,cruel '
print(line)
print('@ line.rstrip() >>> ', line.rstrip())
#
#para ver mas opciones para Strings
#usar dir('string')
print('buscar posicion @ var.find(caracteres) >>> ', name.find('a'))
print('sustituir caracteres @ name.replace(OLD, NEW) >>> ', name.replace('ky', 'ggg'))
print('@string.endswith("char") string.startswith("char") >>> ', name.endswith('ggg'), name.startswith('w'))
print('formato @ "{0} = {1}".format("pi", 3.141516)', '{0} = {1}'.format('pi', 3.141516))

