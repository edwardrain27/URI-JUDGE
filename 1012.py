
#3.0 4.0 5.2

#TRIANGULO: 7.800
#CIRCULO: 84.949
#TRAPEZIO: 18.200
#QUADRADO: 16.000
#RETANGULO: 12.000

values = input()
cadena = values.split(' ')
pi=3.14159

triangle = float(cadena[0])*float(cadena[2])/2
circle = pi*float(cadena[2])**2
trapeze = (1.0/2)*(float(cadena[0])+float(cadena[1]))*float(cadena[2])
square = float(cadena[1])**2
rectangle = float(cadena[0])*float(cadena[1])

print('TRIANGULO: {:.3f}'.format(triangle))
print('CIRCULO: {:.3f}'.format(circle))
print('TRAPEZIO: {:.3f}'.format(trapeze))
print('QUADRADO: {:.3f}'.format(square))
print('RETANGULO: {:.3f}'.format(rectangle))

