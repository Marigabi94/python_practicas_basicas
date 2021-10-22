"""
Practica #7 Listas.

"""


listaRedes = ['Facebook', 'Twitter', 'Instagram', 'Pinterest']
ListaPersona = ['Maria', 27, True, 15.5]
lista3 = ['Lista Redes: ', ['Facebook', 'Twitter', 'Instagram', 'Pinterest']]
lista4 = ['Lista Redes: ', listaRedes]

print(listaRedes, '\n', ListaPersona, '\n', lista3, '\n', lista4)


"""
              0         1           2           3
Lista = ['Facebook', 'Twitter', 'Instagram', 'Pinterest']

pos_final = n-1, Donde n: Numero de elementos de la lista

"""

print(listaRedes[3], '\n', lista3[1][0], '\n', lista4[1][2])

"""


Redefinir lista3


"""
lista3.append(20)

print(lista3)