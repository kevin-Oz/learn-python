# creando archivo txt
file = open('data.txt', 'w')
file.write('Hello world \n')
file.close()
# leyendo archivo
file = open('data.txt')
text = file.read()
print(text)

