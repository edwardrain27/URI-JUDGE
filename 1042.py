numbers = input()

values = numbers.split(' ')

x = int(values[0])
y = int(values[1])
z = int(values[2])


if x == y and x == z:
    print()
    print()
    print()
elif x > y and x > z:
    if y > z:
        print('{}'.format(z))
        print('{}'.format(y))
        print('{}'.format(x))
    else:
        print('{}'.format(y))
        print('{}'.format(z))
        print('{}'.format(x))
elif y > x and y > z:
    if x > z:
        print('{}'.format(z))
        print('{}'.format(x))
        print('{}'.format(y))
    else:
        print('{}'.format(x))
        print('{}'.format(z))
        print('{}'.format(y))
elif z > x and z > y:
    if x > y:
        print('{}'.format(y))
        print('{}'.format(x))
        print('{}'.format(z))
    else:
        print('{}'.format(x))
        print('{}'.format(y))
        print('{}'.format(z))

print('')
for i in values:
    print('{}'.format(i))