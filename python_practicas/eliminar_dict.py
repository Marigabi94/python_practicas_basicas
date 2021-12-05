"""
Practica de como eliminar valores en el diccionario
    
"""

diccionario = {
        1:"Hola", 
        2: "como estas",
        3:"Bien"
    }

print(diccionario)

del diccionario[1]

print(diccionario)


diccionario = {
        1:"Hola", 
        2: "como estas",
        3:"Bien"
    }

valor_eliminado = diccionario.pop(2)
print(valor_eliminado)

diccionario.clear()
print(diccionario)




