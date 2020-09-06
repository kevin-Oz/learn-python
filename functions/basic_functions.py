# funciones***** podemos agregar valores por defecto
def super_hero(nombre='no name', poder='ninguno'):
    print('soy ', nombre, 'y mi poder es ', poder)


super_hero("wolverine", "regeneración")
super_hero()
# tambien puede resibir como parametro una lista pero la funcion espera argumentos separdos
#  colocar * a la lista ---> super_hero(*lista)
# o si los datos estan en un diccionario colocar 2 asteriscos ----> super_hero(**diccionario)

# listas como parametros
print('\n')


def super_heroes(alias):
    listado = ''
    for nick in alias:
        listado += nick + " - "
    print(listado)


superHumanos = ['superman', 'aquaman', 'wonder woman', 'dr strange']
super_heroes(superHumanos)

print('\n')


# parametros arbitrarios
def super_humanos(*lista):
    for value in lista:
        print(value)


super_humanos('flash', 'spiderman')

## diccionarios como parametros
print('\n')


def heroe_s(**heroes):
    print(heroes)
    print(heroes['hero1'])


# el uso de diccionarios permite enviar varios parametros clave valor
heroe_s(hero1='batman', hero2='spiderman')


## tambien se puede combinar parametros

def super_villanos(villano, *villianos, **mas_villanos):
    print('parametro fijo -> ', villano)
    for evil in villianos:
        print('parametro lista -> ', evil)
    print('parametros documento --> ', mas_villanos)


# los parametros mas especificos deben de ir mas a la izquierda
super_villanos('joker', 'el pinguino', 'king pink', evil1='duende verde', evil2='acertijo')


# funciones con retorno

def sumar_numeros(num1, num2):
    return num1 + num2


result = sumar_numeros(2, 3)
print('resultado de la suma 2+3 ->', result)
