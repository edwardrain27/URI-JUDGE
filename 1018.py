
amount = int(input())


cien = amount//100

r1 = amount-100*cien

cincuenta = r1//50

r2 = r1-50*cincuenta

veinte = r2//20

r3 = r2-veinte*20

diez = r3//10

r4 = r3-diez*10

cinco = r4//5

r5 = r4-cinco*5

dos = r5//2

mil = r5-dos*2


print(amount)
print('{} nota(s) de R$ 100,00'.format(cien))
print('{} nota(s) de R$ 50,00'.format(cincuenta))
print('{} nota(s) de R$ 20,00'.format(veinte))
print('{} nota(s) de R$ 10,00'.format(diez))
print('{} nota(s) de R$ 5,00'.format(cinco))
print('{} nota(s) de R$ 2,00'.format(dos))
print('{} nota(s) de R$ 1,00'.format(mil))





