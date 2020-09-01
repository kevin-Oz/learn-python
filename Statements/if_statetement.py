print('IF STATEMENT')
if not 1:
    print('true')
else:
    print('false')

saludo = 'hola cosita'
if saludo == 'hola':
    print('hola')
elif saludo == 'mundo':
    print('mundo')
else:
    print('hola mundo')

branch = {
    'spam': 1.25,
    'ham': 1.99,
    'eggs': 0.99
}
print(branch.get('spam', 'Bad choice'))
print(branch.get('bacon', 'Bad choice'))
# operando con or
print(3 or 5)
a = 1
b = 2
x = 10
# ternario
z = a if 1 else b
print(z)
z = ((a and b) or x)
print(z)
##
# vacio significa falso, mientras que
# si hay texto lo interpreta como true
msj = 'true' if 'noempty' else 'false'
print(msj)
msj = 'true' if '' else 'false'
print(msj)
