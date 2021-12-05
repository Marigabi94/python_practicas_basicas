"""
Practica de args y kwargs (argumentos)

"""


def multiplicar(valor,valor2,valor3):
    resultado = 1
    resultado *= valor
    resultado *= valor2
    resultado *= valor3
    return resultado
print(multiplicar(6,1,2))

def multiplicar2(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

print(multiplicar2(6,1,2))


def multiplicar3(inicio,*args,**kwargs):
    print(kwargs)
    for i in args:
        inicio *= i
    return inicio

print(multiplicar3(20,12,4,56,5,3, cancelacion = 50))



