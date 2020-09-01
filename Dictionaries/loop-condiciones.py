
keyvalue = {'a': 1, 'c': 3, 'b': 2}
#for
print('\n FOR - WHILE')
for k in keyvalue:
    print(k, '>>> ', keyvalue[k])
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


