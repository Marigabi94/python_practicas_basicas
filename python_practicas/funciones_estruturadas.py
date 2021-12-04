""""
Practica de funciones estructuradas

"""

lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ("Hola","Venezuela","Maria")


lista_to_topla = tuple(lista)

print(lista_to_topla)

tupla_to_list=list(tupla)

print(tupla_to_list)


#TODO: Agregar valores 
lista.append(15)
lista.insert(2,18)
print(lista)

#TODO: eliminar valores
lista.remove(18) #Elimina el valor indicado
print(lista)

lista.pop(3) #elimina es la posicion que se indica
print(lista)


#TODO: retorna un valor
valor = lista.pop(2)
print(valor)

#TODO: retornar cantidad de valor repetido
cantidad = lista.count(2)
print(cantidad)


#TODO: unir 2 Listas
lista.extend(tupla_to_list)
print(lista)

#TODO: copiar elementos de una lista en otra lista
tupla_to_list = lista.copy()
print(tupla_to_list)

#TODO: limpiar lista
lista.clear()
print(lista)


