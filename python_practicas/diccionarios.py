"""
Practica de diccionarios

"""

diccionario = {
        1:"Hola", 
        2: "como estas",
        3:"Bien"
    }

print(diccionario)

# imprime la clave 1
print(diccionario[1])


# devuelve true o false dependiendo si existe o no la clave.
resultado = 1 in diccionario
print(resultado)


# devuelve el contenido de la clave 2
resultado = diccionario.get(2)
print(resultado)


# si la clave solicitada no existe devuelve el mensaje establecido 
resultado = diccionario.get(0, "No exite un valor asociado a esta clave")
print(resultado)


# agregar una nueva clave y dato
diccionario[4]= "nuevo"
print(diccionario)
