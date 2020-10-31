values = input()
abc = values.split(' ')
a = float(abc[0])
b = float(abc[1])
c = float(abc[2])

#ax^2+bx+c

arg = b**2-4*a*c

if arg < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b+(arg)**(1/2))/(2*a)
    r2 = (-b-(arg)**(1/2))/(2*a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))