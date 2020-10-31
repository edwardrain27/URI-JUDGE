values = input()
cadena = values.split(' ')
N1 = float(cadena[0])
N2 = float(cadena[1])
N3 = float(cadena[2])
N4 = float(cadena[3])
media = (N1*2+N2*3+N3*4+N4*1)/10

if media >= 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media >=5 and media <=6.9:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    nota = float(input())
    print('Nota do exame: {:.1f}'.format(nota))
    media = (media+nota)/2
    if media >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media))
    elif media <= 4.9:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media))
        
else:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')