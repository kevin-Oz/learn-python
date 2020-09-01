[a, b, c] = (1, 2, 3)
print(a, b, c)
(a, b, c) = 'ABC'
print(a, b, c)
((a, b), c) = ('SP', 'AM')
print(a, b, c)
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)
L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

secuencia = [1, 2, 3, 4]
print('\nsecuencia\n', secuencia)
a, b, c, *d = secuencia
print(a, b, c, d)
print('\nasignacion por referecia\n @a = b = []\nb.append(42) >>> ')
# el valor de a y b apuntan a la misma direccion en memoria
a = b = []
b.append(42)
print(a, b)
# asignaciones
'''
X += Y X &= Y X -= Y X |= Y
X *= Y X ^= Y X /= Y X >>= Y
X %= Y X <<= Y X **= Y X //= Y
'''






