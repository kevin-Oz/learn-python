name = 'kevin'
print('tamanio de la palabra ->', len(name))  # length de la palabra
print('obtener caracter por posicion ', name[2])
print('obtener el caracter por posicion inversa', name[-1])
print('obtener un rango de caracteres', name[1:3])
#
# con name[:] -> obtiene todos los caracteres
# name[:3] -> obtiene los caracteres del 0 al 3
print('concatenar caaracteres: ', name + 'aaa')
#
print('para multipicar palabras usar *asterisko*', name * 3, '\n')
#
print('IMMUTABILIDAD')
name = 'K' + name[1:]
print(name, '\n')
#
print('**otras operaciones con strings**')
print('buscar posicion [var.find(caracteres)] > ', name.find('in'), '\n')
print('sustituir caracteres ', name.replace('in', 'ggg'))
