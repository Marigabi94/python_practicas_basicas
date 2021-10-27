"""
 Practica #11 Funciones
 
 
"""


def sumar():
    numero = int(input('Ingrese primer numero para la suma: '))
    numero2 = int(input('Ingrese segundo numero para la suma: '))

    suma = numero + numero2
    print('Resultado de suma de los numeros ingresados: ' +str(suma))

for i in range(2):
    sumar()

def restar(num, num2):
    resta = num - num2
    return resta
  

for i in range(2):
    num = int(input('Ingrese primer numero para la resta: '))
    num2 = int(input('Ingrese segundo numero para la resta: '))
   
    print('Resultado de resta de los numeros ingresados:'+str(restar (num,num2)))

