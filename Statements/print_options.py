import sys
print('\nPRINT options')
sys.stdout.write('hola\n')
# !print([object, ...][, sep=' '][, end='\n'][, file=sys.stdout])
a = 'spam'
b = 88
c = ['we']
print(a, b, c)
#cambiar el separador con sep
print('@print sep >>>  ', a, b, c, sep='**')
# imprimir formato al final
print('@print end >>>  ', a, b, c, end='...\n')
# redirigir la salida standar
log = open('log.txt', 'a')
print(a, b, c, file=log)
print(open('log.txt').read())




