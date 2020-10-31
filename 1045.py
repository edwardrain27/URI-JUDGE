

values = input().split(' ')

values = [ float(x) for x in values]

values.sort(reverse=True)

a = values[0]
b = values[1]
c = values[2]


if a >= b+c:
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2+c**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2+c**2:
    print('TRIANGULO OBTUSANGULO')
    if (a==b and a!=c) or (a==c and a!=b) or (b==c and c!=a):
        print('TRIANGULO ISOSCELES')
    
elif a**2 < b**2+c**2:
    print('TRIANGULO ACUTANGULO')
    if a==b==c:
        print('TRIANGULO EQUILATERO')
    else:
        print('TRIANGULO ISOSCELES')


