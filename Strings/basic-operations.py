name = 'kevin'
print('tamanio de la palabra @ len(string) >>> ', len(name))  # length de la palabra
print('obtener caracter por posicion @ string[0] >>> ', name[2])
print('obtener el caracter por posicion inversa @string[-1] >>> ', name[-1])
print('obtener un rango de caracteres @name[1:3] >>> ', name[1:3])
#
# con name[:] -> obtiene todos los caracteres
# name[:3] -> obtiene los caracteres del 0 al 3
print('concatenar strings @name + \'haa\' >>> ', name + 'aaa')
#
print('para multipicar palabras @ name * 3 >>> ', name * 3, '\n')
#
print('IMMUTABILIDAD')
name = 'K' + name[1:]
print(name, '\n')
#
print('**otras operaciones con Strings**')
abecedario = 'abcdefghijklmnopqrstuvxyz'
#mostrar caracters a partir de la posicion 1 hasta 10 con un paso de 2 string[1:10:2]
print('@string[1:10:2] >>> ', abecedario[1:10:2])
#mostrar caracters a partir de la posicion inicial hasta el final con un paso de 2 string[::2]
print('@string[::2] >>> ', abecedario[::2])
print('@string[slice(1, 3)] >>> ', 'string'[slice(1, 3)])
print('\nCONVERSIONES')
print('str(3.141516), float("1.4"), int("5") >>> ', str(3.1415), float('1.4'), int('5'))

x = set('spam')
print('X: ', x)
y = {'h', 'a', 'm'}
print('Y: ', y)
#interseccion, elementos que coinciden en ambos Dictionaries
print('interseccion : x & y  >> ', x & y)
print('Union (sin repeticion)  : x | y  >> ', x | y)
print('diferencia : x - y  >> ', x - y)

