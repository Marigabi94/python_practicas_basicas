"""
Practica de funciones lambdas

"""


def potencia (numero,exponente):
    numero = pow(numero,exponente)
    return numero
print(potencia(8,2))


def potencia (numero,exponente):
    return pow(numero,exponente)
print(potencia(8,2))

# funcion lambda:
potencia = lambda numero, exponente : pow(numero,exponente)
print(potencia(10,2))

multiplicar_por_10 = lambda numero: numero*10       
potencia = lambda numero, exponente : pow(multiplicar_por_10(numero),exponente)
print(potencia(10,2))

