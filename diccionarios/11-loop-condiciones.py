
keyvalue = {'a': 1, 'c': 3, 'b': 2}
print('diectorio >>> ', keyvalue)
keyDirectory = list(keyvalue.keys())
print('keys >>', (keyDirectory))
keyDirectory.sort()
print('sort >>> ', (keyDirectory))
#for
print('\n FOR - WHILE')
for k in keyvalue:
    print(k, '=>', keyvalue[k])
contador = 4
##
#while
while contador > 0:
    print('spam! ' * contador)
    contador -= 1
##
print('\nCONDICIONES')
print('| <valor> in <documento> | >>', 'd' in keyvalue)
print('| if not <valor> in <document>: | >>> ')
if not 'e' in keyvalue:
    print('missing')
valor = keyvalue['x'] if 'x' in keyvalue else 0
print(valor, '\n')
#
#   tuplas
print('TUPLAS')
tupla = (1, 2, 3, 4)
print('tupla > ', tupla, 'size: ', len(tupla))
tupla += (5, 6)
print('concatenacio'
      'n | tupla + (5, 6) | >> ', tupla)



