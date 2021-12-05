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

#forma 1 de recorrer un diccionario
for clave,valor in diccionario.items():
    print("{0} --> {1}".format(clave,valor))


#forma 2 de recorrer un diccionaro con este se valida en caso de error
for clave in diccionario:
    resultado = diccionario.get(clave, "No exite un valor asociado a esta clave")
    print(resultado)
    

#guardar los valores en una variable
valores = diccionario.values()
print(valores)

#recorrer los valores
for valor in valores:
    print(valor)
    


# o en resumen:
for valor in diccionario.values():
    print(valor)
    


# imprimir solo las claves
for clave in diccionario.keys:
    print(clave)
    

    
