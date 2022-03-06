from array import array


cadena_texto = array(str('u'), input('Ingrese su cadena de texto:'))




llave_abierta = cadena_texto.count('{')
llave_cerrada = cadena_texto.count('}')
parentesis_abierta = cadena_texto.count('(')
parentesis_cerrado = cadena_texto.count(')')
corchete_abierto = cadena_texto.count('[')
corchete_cerrado = cadena_texto.count(']')

print(cadena_texto)

def llavesPrint( llave_abierta, llave_cerrada):
    print('Total de llaves abiertas:', llave_abierta)
    print('Total de llaves cerradas:', llave_cerrada)
    
    if (llave_abierta > llave_cerrada):
        llaves_cerradas_faltantes = int(llave_abierta) - int(llave_cerrada)
        print('El numero de llaves cerradas que faltan es:', llaves_cerradas_faltantes )
    elif (llave_cerrada > llave_abierta):
        llaves_abiertas_faltantes = int(llave_cerrada) - int(llave_abierta)
        print('El numero de llaves abiertas que faltan es:', llaves_abiertas_faltantes)
    else:
        print('Llaves abiertas y cerradas completas')

def parentesisPrint( parentesis_abierta, parentesis_cerrada):
    print('Total de parentesis abiertas:', parentesis_abierta)
    print('Total de parentesis cerradas:', parentesis_cerrada)
    
    if (parentesis_abierta > parentesis_cerrada):
        parentesis_cerradas_faltantes = int(parentesis_abierta) - int(parentesis_cerrada)
        print('El numero de parentesis cerradas que faltan es:', parentesis_cerradas_faltantes )
    elif (parentesis_cerrada > parentesis_abierta):
        parentesis_abiertas_faltantes = int(parentesis_cerrada) - int(parentesis_abierta)
        print('El numero de parentesis abiertas que faltan es:', parentesis_abiertas_faltantes)
    else:
        print('Parentesis abiertos y cerrados completos')

def corchetePrint( corchete_abierta, corchete_cerrada):
    print('Total de corchete abiertas:', corchete_abierta)
    print('Total de corchete cerradas:', corchete_cerrada)
    
    if (corchete_abierta > corchete_cerrada):
        corchete_cerradas_faltantes = int(corchete_abierta) - int(corchete_cerrada)
        print('El numero de corchete cerradas que faltan es:', corchete_cerradas_faltantes )
    elif (corchete_cerrada > corchete_abierta):
        corchete_abiertas_faltantes = int(corchete_cerrada) - int(corchete_abierta)
        print('El numero de corchete abiertas que faltan es:', corchete_abiertas_faltantes)
    else:
        print('Corchetes abiertos y cerrados completos')


llavesPrint(llave_abierta, llave_cerrada)
corchetePrint(corchete_abierto, corchete_cerrado)
parentesisPrint(parentesis_abierta, parentesis_cerrado)