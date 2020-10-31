point1 = input()
point2 = input()

chain1 = point1.split(' ')
chain2 = point2.split(' ')

x1 = float(chain1[0])
x2 = float(chain2[0])
y1 = float(chain1[1])
y2 = float(chain2[1])

distance = ((x2-x1)**2+(y2-y1)**2)**(1/2)

print('{:.4f}'.format(distance))