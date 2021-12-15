sumar = lambda numero, suma: suma + numero

def calcular_suma_elementos(suma= 0):
    while True:
        try:
            cantidad_elementos = int(input("Ingrese la cantidad de elementos que desea sumar: "))
        except ValueError:
            print("Error, por favor ingrese un número")        
        except Exception as e:
            print(type(e).__name__)
        else:
            break
        finally:
            print("\n\n------> Ahora siga la instrucciones para ingresar los números de la suma...\n")
    for i in range (cantidad_elementos):
        while True:
            try:
                numero = int(input("Ingrese el numero que desea agregar a la suma: "))
            except ValueError:
                print("Error, por favor ingrese un número")
            except Exception as e:
                print(type(e).__name__)
            else: 
                break
        suma = sumar(numero,suma)
    
    print(f"La suma de los elementos ingresados es: {suma}")


# calcular_suma_elementos()

def dividir():  
    while True:
        try:
            numero = int(input("Ingrese un número:"))
            division =40/numero
            print(division)
        
        except ValueError:
            print("--------------Ingrese un número!--------------")
        except ZeroDivisionError:
            print("--------------No se puede realizar una division entre 0!--------------")
        except Exception as e:
            print(type(e).__name__)
        else: 
            break
    
dividir()        