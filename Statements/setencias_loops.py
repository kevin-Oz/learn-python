x = 5
y = 3
# es importante la identacion para saber
# cuando termina una instruccion
if x > y:
    x = 1
    y = 2
print(x, y)
#
## bucle while con sentencia if
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Err! ' * 3)
    else:
        print(int(reply) ** 2)
    print(reply.upper())
print('end')
##
print('\nTry statements')
while True:
    reply = input(' >>> ')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Err ¡ ' * 3)
    else:
        print(int(reply) * 2)
print('bye')
