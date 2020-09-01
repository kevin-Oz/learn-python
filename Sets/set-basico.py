set1 = set('abcdef')
set2 =set('bdxyz')
print(set1, set2)
#
print('pertenencia @ \'e\' in set1 >>>', 'e' in set1)
print('diferencia @ set1 - set2 >>> ', set1 - set2)
print('Union @ set1 | set2 >>> ', set1 | set2)
print('interseccion(coincidentes) @ set1 & set2 >>> ', set1 & set2)
print('sin repeticion @ set1 ^ set2 >>> ', set1 ^ set2)
#añadir elementos
set1.add(23)
print('añadiendo elemento @ set.add(\'23\')', set1)
