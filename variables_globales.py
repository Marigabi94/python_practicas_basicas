nombre = 'Maria' # variable global


def mostrar_nombre():
    global nombre_2 
    nombre_2 = 'Fran'
    print(nombre_2)
  

mostrar_nombre()
print(nombre)
nombre_2 = "Lucky"
print(nombre_2)

