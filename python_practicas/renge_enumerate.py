"""
Prctica de la funciones range y enumerate


"""

#lista de numeros del 0 al 25
for valor in range(26):
    print(valor)
    

print('\n')
#lista de numeros del 15 al 25    
for valor in range(15,26):
    print(valor)
    
print('\n')
#numeros impares desde el 1 hasta el 25
for valor in range(1,26,2):
    print(valor)

print('\n')


lista =[1,2,3,4,5,6,7,8,9]
for valor in range(len(lista)):
    print(lista[valor])
    
print('\n')



#devuelve sus posiciones con su respectivo valor
lista =[1,2,3,4,5,6,7,8,9]
for valor in enumerate(lista):
    print(valor)
    

for posicion, valor in enumerate(lista):
    print("El valor {0} esta en la posicion {1}".format(valor,posicion))

