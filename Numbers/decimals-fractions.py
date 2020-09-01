import decimal
from fractions import Fraction
print('import decimal \nfrom fractions import Fraction')
print('DECIMALES')
##formato de decimales
div = 1 / 3
print('@1/3 >>> ', div)
print('notacion expornencial @ \'%e\' %1/3 >>> ', '%e' % div)
print('Dos decimales @ \'%4.2f\' %1/3 >>> ', '%4.2f' % div)
print('Dos decimales @ \'{0:4.2f}\'.format(1/3) >>> ', '{0:4.2f}'.format(div))
d = decimal.Decimal('3.141')
print('@decimal.Decimal(\'3.141\') + 1 >>> ', d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
f = Fraction(2, 3)
f = Fraction(2, 3)
print('\nFRACIONES\n', f + 1)
print(f + Fraction(1, 2))
