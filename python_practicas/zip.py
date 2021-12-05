"""
Union del contenido de listas y duplas 

"""

lista = [1,2,3,4,5,6,7,8,9]
tupla= ('hola','dos','tres','cuatro','cinco')

union,union1,union2 = lista[0], lista[1], lista[2]
print(union)
print(union1)
print(union2)


union,*union1,union2 = lista
print(union)
print(union1)
print(union2)

#Unir lista y tupla e imprimirla como lista
union = list(zip(lista,tupla))
print(union)

#Unir lista y tupla e imprimirla como tupla
union = tuple(zip(lista,tupla))
print(union)

#Unir lista y tupla e imprimirla como diccionario
union = dict(zip(lista,tupla))
print(union)

#zip toma la lista o tupla de menor cantidad de valores
#para definir el maximo de volores que tendra la agrupacion 
# y lo demas lo descarta.

lista2 = ['12','13','14',(9,8,7)]
union = list(zip(lista,tupla,lista2))
print(union)

