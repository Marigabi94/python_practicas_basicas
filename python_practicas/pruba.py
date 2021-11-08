n =     int(input('Ingrese un número positivo:'))

 
if n >0:
    for i in range(0, n):

        print('{0:2d} x {1:3d} = {2:4d}'.format(i+1, n, (i+1)*n))
else:
   print('Número negativo')
    

    