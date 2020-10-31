
numbers = input()
values = numbers.split(' ')
a = float(values[0])
b = float(values[1])
c = float(values[2])



if a < c+b and c < a+b and b < a+c:
    Petrimetro = a+b+c
    print('Perimetro = {:.1f}'.format(Petrimetro))
else:
    area = (1/2)*(a+b)*c
    print('Area = {:.1f}'.format(area))