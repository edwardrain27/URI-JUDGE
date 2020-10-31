
amount = float(input())

entera = int(amount // 1)
decimal = int((amount%1)*100)


hundred = entera // 100
fifty = (entera%100)//50
twenty =((entera%100)%50) // 20
ten = (((entera%100)%50)%20) // 10
five = ((((entera%100)%50)%20)%10) // 5
two = (((((entera%100)%50)%20)%10)%5) // 2
one = ((((((entera%100)%50)%20)%10)%5)%2)

fiftycents = decimal//50
twentyfivecents = (decimal%50) // 25
tencents = ((decimal%50)%25) // 10
fivecents = (((decimal%50)%25)%10) // 5
onecents = (((decimal%50)%25)%10)%5




print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(hundred))
print('{} nota(s) de R$ 50.00'.format(fifty))
print('{} nota(s) de R$ 20.00'.format(twenty))
print('{} nota(s) de R$ 10.00'.format(ten))
print('{} nota(s) de R$ 5.00'.format(five))
print('{} nota(s) de R$ 2.00'.format(two))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(one))
print('{} moeda(s) de R$ 0.50'.format(fiftycents))
print('{} moeda(s) de R$ 0.25'.format(twentyfivecents))
print('{} moeda(s) de R$ 0.10'.format(tencents))
print('{} moeda(s) de R$ 0.05'.format(fivecents))
print('{} moeda(s) de R$ 0.01'.format(onecents))



