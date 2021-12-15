"""
Practica de decoradores

"""
def funcion_decoradora(funcion):
    def nueva_funcionalidades():
        print ('Buenas madrugadas')
        funcion()
        print('buenas tardes')
    return nueva_funcionalidades

@funcion_decoradora
def saludo():
    print('Hola buenos dias')
    
saludo()


def funcion_decoradora2(funcion):
    def nueva_funcionalidades(*arg,**kwargs):
        print ('Antes de multiplicar')
        resultado = funcion(*arg,**kwargs)
        print(resultado)
        print('despues de multiplicar')
    return nueva_funcionalidades

@funcion_decoradora2
def multiplicar(num,num2):
    return num * num2
    
multiplicar(90,2)
