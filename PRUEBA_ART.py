import random


# Defino la función inicial
def numale15():
    numero = random.randint(1, 5)
    return numero


# Compruebo que funciona
resultado1 = numale15()
print("El número premiado es el...", resultado1)


# Tengo que utilizar en una segunda función la priemra de tal manera que en vez de ser los números enteros del 1 al 5 sean del 1 al 7
# Se me han ocurrido varias opciones para solucionar el problema

#-------------------------------------------------
# SOLUCIÓN1
def solucion1():
    lista_numeros = [numale15(), 6, 7]
    numero2 = random.choice(lista_numeros)
    return numero2


resultado2 = solucion1()
print("Solución 1:", resultado2)


#--------------------------------------------------
# SOLUCIÓN2
def solucion2():
    numero3 = numale15()
    if numero3 == 5:
        return random.choice([5, 6, 7])
    return numero3


resultado3 = solucion2()
print("Solución 2:", resultado3)


#----------------------------------------------------
# SOLUCIÓN3

valores = random.randint(6, 7)
valores2 = numale15()

def solucion3():
    numerito = []
    numerito.append(valores)
    numerito.append(valores2)
    completo = random.choice(numerito)
    return completo


resultado4 = solucion3()
print("Solución 3:", resultado4)


