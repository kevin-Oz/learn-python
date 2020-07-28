name = 'wasovsky'
age = '32'
frutas = 'banana,uva,fresa,mango'
print('lista de frutas [split] >>', frutas.split(','), '\n')
#
print('UPPER - LOWER')
print(frutas.upper())
print(frutas.lower(), '\n')
#
print('verificar si es texto o numero el string \n ', name.isalpha(), age.isdigit())
#
line = 'hola mundo,cruel '
print(line)
print(line.rstrip())
#
#para ver mas opciones para strings 
#usar dir('string')

x = set('spam')
print('X: ', x)
y = {'h', 'a', 'm'}
print('Y: ', y)
#interseccion, elementos que coinciden en ambos diccionarios
print('interseccion : x & y  >> ', x & y)
print('Union (sin repeticion)  : x | y  >> ', x | y)
print('diferencia : x - y  >> ', x - y)