print('\nWhile loop')
x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]
#
print('\n')
a = 0
b = 10
while a < b:
    print(a, end=' ')
    a += 1
print('\n')
'''
break
Jumps out of the closest enclosing loop (past the entire loop statement)
continue
Jumps to the top of the closest enclosing loop (to the loop’s header line)
pass
Does nothing at all: it’s an empty statement placeholder
Loop else block
Runs if and only if the loop is exited normally (i.e., without hitting a break )
'''
y = 10
while y:
    y -= 1
    if y % 2 != 0: continue
    print(y, end=' ')
#
while True:
    name = input('Enter name:')
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age))
##
#
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')

