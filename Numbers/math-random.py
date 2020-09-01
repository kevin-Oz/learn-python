#importando librerias
import math
import random
print('import math \nimport random')
# numero pi
print('Pi  @math.pi >>> ', math.pi)
#obteniendo raiz cuadrada
print('Raiz de 4 : @math.sqrt(4) >>> ', math.sqrt(4))
## diferencias entre trunc y floor
## floor siguiente integer mas bajo
## trunc eliminar decimales
print('\n @math.floor(2.5) >>> ', math.floor(2.5))
print(' @math.floor(-2.5) >>> ', math.floor(-2.5))
print(' @math.trunc(2.5) >>> ', math.trunc(2.5))
print(' @math.trunc(-2.5) >>> ', math.trunc(-2.5))
#
print('\n @ pow(2,4) o 2**4 >>> ', pow(2, 4))
print(' @ abs(-5.6) >>> ', abs(-5.6))
print(' @ sum((2,4,2))  >>> ', sum((2, 4, 2)))
#
print('\nround @[round(2.567), round(2.456), round(2.567, 2)]>>> ', [round(2.567), round(2.456), round(2.567, 2)])
#
print('\nnumero random @random.random() >>> ', random.random())
print('numero random entre 1-4 @random.choice([1, 2, 3, 4]) >>> ', random.choice([1, 2, 3, 4]))
print('numero random entero @random.randint(1, 10) >>> ', random.randint(1, 10))


