
values = input()

cadena = values.split(' ')

maior1 = int((1/2)*(int(cadena[0])+int(cadena[1])+abs(int(cadena[0])-int(cadena[1]))))
maior2 = int((maior1 + int(cadena[2])+abs(maior1-int(cadena[2])))/2)


print('{} eh o maior'.format(maior2))