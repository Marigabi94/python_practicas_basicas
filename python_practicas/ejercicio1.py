"""

Numero ingresado por consola es par o impar y ademas si es negativo o positivo

"""

print('\n\t\t\t\tEjercicio 1')

num= int(input('Ingrese un numero: \n'))

if num%2 ==0:
    if num >0:
        print('\nEl numero ingresado es par y tambien es positivo')
    else: 
        print('\nEl numero ingresado es par y tambien es negativo')

else:
    if num >0:
        print('\nEl numero ingresado es impar y tambien es positivo')
    else: 
        print('\nEl numero ingresado es impar y tambien es negativo')