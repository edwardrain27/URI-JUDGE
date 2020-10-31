
producto1 = input()
producto2 = input()

cadena1=producto1.split(' ')
cadena2=producto2.split(' ')

total = float(cadena1[1])*float(cadena1[2])+float(cadena2[1])*float(cadena2[2])

print('VALOR A PAGAR: R$ {:.2f}'.format(total))