    """
        Practica de conjunto
    """

#TODO: conjunto vacio
conjunto = set()
print(conjunto)

#TODO: conjunto con datos
conjunto = {1,2,3}
print(conjunto)


#TODO: agregar dato
conjunto.add(10)
print(conjunto)

conjunto.add("Maria")
print(conjunto)

#TODO: por regla  no existen valores repetidos dentro de un conjunto
conjunto = {1,2,3,3,3,3,5,5,9,9,9,9}
print(conjunto)


#TODO: eliminar datos repetidos de una lista usando conjunto (opcion 1)
lista = [1,2,3,3,3,3,5,5,9,9,9,9]
print(lista)
conjunto = set(lista)
lista = list(conjunto)
print(lista)

#TODO: eliminar datos repetidos de una lista usando conjunto (opcion 2)
lista = [1,2,3,3,3,3,5,5,9,9,9,9]
print(lista)
lista = list(set(lista))
print(lista)


#TODO: verificar si un elemento esta en un conjunto
conjunto2 = {1,2,3,3,3,3,5,5,9,9,9,9}
pertenencia = 3 in conjunto2
print(pertenencia)

#devuelve false porque no existe el caracter '9' en el conjunto
pertenencia = '9' in conjunto2
print(pertenencia)

#devuelve true por la negacion.
perenencia = '9' not in conjunto2
print(pertenencia)

#TODO: convierte una cadena de texto en un conjunto, separa la  cadena en valores y eliminas los valores repetidos
cadena = "Esto es una cadena de texto"
cadena = set(cadena)
print(cadena)
